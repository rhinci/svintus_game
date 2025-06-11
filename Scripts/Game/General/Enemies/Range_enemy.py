from Scripts.Game.General.Enemies.Enemy import enemy
from Scripts.Game.Weapon_scripts.Explosion import explosion
from Scripts.Game.General.ItemBox import health_pack, exp_pack
from configs.collectables import HEALTH_PACK, EXP
import math
from random import randint
from Scripts.Game.General.statistics_collector import run_stats

class range_enemy(enemy):
    def __init__(self, all_sprites, enemy_group, mob_group, player, stats, pos, weapon):
        super().__init__(all_sprites, enemy_group, mob_group, player, stats, pos)
        # ... остальная инициализация ...
        self.attack_range = 500
        self.weapon = weapon
        self.retreat_mode = False
        self.retreat_threshold = 0.3  # 30% HP для активации отступления

    def retreat(self):

        # Базовое отступление от игрока
        dx = self.rect.centerx - self.player.rect.centerx
        dy = self.rect.centery - self.player.rect.centery
        distance = max(1, math.sqrt(dx ** 2 + dy ** 2))

        # Основное направление отступления
        retreat_direction = (dx / distance, dy / distance)

        # Добавляем случайное отклонение для непредсказуемости
        angle_variation = math.radians(randint(-50, 50))
        new_direction = (
            retreat_direction[0] * math.cos(angle_variation) - retreat_direction[1] * math.sin(angle_variation),
            retreat_direction[0] * math.sin(angle_variation) + retreat_direction[1] * math.cos(angle_variation)
        )

        retreat_speed = self.spd * 1.5
        self.velocity = [
            new_direction[0] * retreat_speed,
            new_direction[1] * retreat_speed
        ]

    def death(self):
        chance = randint(0, 100)
        if 0 <= chance <= 25:
            health_pack(self.all_sprites, HEALTH_PACK, self.player, self.rect.center)
        elif 25 < chance <= 50:
            exp_pack(self.all_sprites, EXP, self.player, self.rect.center)

        explosion(self.all_sprites, self.mob_group, self.rect.center, (100, 100))
        self.kill()  # Удаляем из всех групп
        run_stats.increment_stat("1. Kills", 1)
        self.alive = False  # Помечаем как мертвого
        # Дополнительная очистка (опционально)
        self.all_sprites.remove(self)
        self.enemy_group.remove(self)
        self.mob_group.remove(self)
        self.weapon.kill()

    def attack(self):
        self.weapon.fire(self.player.pos)

    def update(self):
        if not self.is_alive():
            return

        # Проверяем, нужно ли перейти в режим отступления
        if not self.retreat_mode and self.curr_hp <= self.max_hp * self.retreat_threshold:
            self.retreat_mode = True

        distance_to_player = math.sqrt(
                (self.player.pos[0] - self.rect.centerx) ** 2 +
                (self.player.pos[1] - self.rect.centery) ** 2
            )
        if self.retreat_mode:
            self.retreat()
            # В режиме отступления все равно можно атаковать
            if distance_to_player <= self.attack_range * 1.2:  # +20% к дистанции атаки
                self.attack()
        else:
            # Обычное поведение
            if distance_to_player <= self.attack_range:
                self.attack()
            else:
                self.move()

        # Общие обновления
        self.border()
        self.animation()
        self.collision()
        self.weapon.rect.center = self.rect.center
        if self.weapon != None:
            self.weapon.rotate(self.player.pos)
        if self.curr_hp <= 0:
            self.death()
