import pygame as pg
import random as r
from Scripts.Game.General.Enemies.Melee_enemy import melee_enemy
from Scripts.Game.General.Enemies.Range_enemy import range_enemy
from configs.enemy_config import MELEE_ENEMY, RANGE_ENEMY
from Scripts.Game.Weapon_scripts.Mashinegun import mashineGun
from Scripts.Game.Weapon_scripts.Blaster import blaster
from Scripts.Game.Weapon_scripts.FireThrower import firethrower
from Scripts.Game.Weapon_scripts.LaserGun import lasergun
from configs.enemy_weapon_config import MASHINEGUN, BLASTER,FIRETHROWER, LASERGUN
import math

list_of_enemys = [MELEE_ENEMY, RANGE_ENEMY]
class spawner():
    def __init__(self, all_sprites, enemy_group, mob_group, weapon_group, player, player_group, spawn_cooldown, screen):
        self.spawn_cooldown = spawn_cooldown * 1000  # начальный кд спавна в мс
        self.min_spawn_cooldown = 500  # минимальный кд спавна в мс
        self.all_sprites = all_sprites
        self.enemy_group = enemy_group
        self.mob_group = mob_group
        self.weapon_group = weapon_group
        self.player_group = player_group
        self.target = player
        self.screen = screen
        self.list_of_enemys = list_of_enemys
        self.update_time = pg.time.get_ticks()
        self.game_start_time = pg.time.get_ticks()
        self.max_enemies = 20  # начальный максимум врагов
        self.max_enemies_limit = 40  # абсолютный максимум врагов
        self.difficulty_interval = 30000  # интервал увеличения сложности (30 сек)

        # Статистика для баланса
        self.spawn_count = 0
        self.last_difficulty_increase = 0

    def spawn(self):
        """Генерация позиции спавна с учетом позиции игрока"""
        margin = 400  # минимальное расстояние от игрока
        while True:
            x = r.randint(0, int(self.screen[0]))
            y = r.randint(0, int(self.screen[1]-90))
            # Проверяем, чтобы враги не спавнились слишком близко к игроку
            if math.hypot(x - self.target.rect.centerx, y - self.target.rect.centery) > margin:
                return (x, y)

    def random_weapon(self, pos):
        """Случайный выбор оружия с изменяющимися шансами"""
        current_time = (pg.time.get_ticks() - self.game_start_time) / 1000  # время в секундах
        # Увеличиваем шанс появления мощного оружия со временем
        if current_time > 120:  # после 2 минут
            weights = [30, 25, 15, 10]  # mashineGun, firethrower, blaster, laser
        elif current_time > 60:  # после 1 минуты
            weights = [20, 25, 25, 20]
        else:  # начальные значения
            weights = [40, 20, 30, 5]

        weapon_type = r.choices(
            ['mashineGun', 'firethrower', 'blaster', 'laser'],
            weights=weights
        )[0]

        if weapon_type == 'mashineGun':
            return mashineGun(self.all_sprites, self.mob_group, self.player_group, self.weapon_group, MASHINEGUN, pos)
        elif weapon_type == 'firethrower':
            return firethrower(self.all_sprites, self.mob_group, self.player_group, self.weapon_group, FIRETHROWER, pos)
        elif weapon_type == 'blaster':
            return blaster(self.all_sprites, self.mob_group, self.player_group, self.weapon_group, BLASTER, pos)
        else:
            return lasergun(self.all_sprites, self.mob_group, self.player_group, self.weapon_group, LASERGUN, pos)

    def update_difficulty(self):
        """Автоматическое увеличение сложности со временем"""
        current_time = pg.time.get_ticks()
        # Увеличиваем сложность каждые difficulty_interval миллисекунд
        if current_time - self.last_difficulty_increase > self.difficulty_interval:
            self.last_difficulty_increase = current_time

            # Уменьшаем кд спавна (но не ниже минимума)
            new_cooldown = max(
                self.spawn_cooldown * 0.9,  # уменьшаем на 10%
                self.min_spawn_cooldown
            )
            self.spawn_cooldown = new_cooldown

            # Увеличиваем максимальное количество врагов (но не выше лимита)
            self.max_enemies = min(
                int(self.max_enemies * 1.1),  # увеличиваем на 20%
                self.max_enemies_limit
            )

            # Увеличиваем сложность врагов
            for enemy_type in [MELEE_ENEMY, RANGE_ENEMY]:
                enemy_type['spd'] *= 1.05  # +5% скорости
                enemy_type['atk'] *= 1.03  # +3% атаки
                enemy_type['max_hp'] *= 1.1  # +10% здоровья

    def update(self):
        """Обновление спавнера с учетом сложности"""
        self.update_difficulty()

        current_time = pg.time.get_ticks()
        if (current_time - self.update_time >= self.spawn_cooldown and
            len(self.enemy_group) < self.max_enemies):

            self.update_time = current_time

            # Иногда спавним несколько врагов сразу
            spawn_count = 1
            if r.random() < 0.2:  # 20% шанс на двойной спавн
                spawn_count = 2
            elif r.random() < 0.05:  # 5% шанс на тройной спавн
                spawn_count = 3

            for _ in range(spawn_count):
                pos = self.spawn()
                enemy_type = r.choice(self.list_of_enemys)
                if enemy_type == MELEE_ENEMY:
                    enemy = melee_enemy(
                        self.all_sprites, self.enemy_group, self.mob_group,
                        self.target, MELEE_ENEMY, pos
                    )
                else:
                    weapon = self.random_weapon(pos)
                    enemy = range_enemy(
                        self.all_sprites, self.enemy_group, self.mob_group,
                        self.target, RANGE_ENEMY, pos, weapon
                    )

                # Увеличиваем характеристики врагов в зависимости от времени
                time_scale = (current_time - self.game_start_time) / 60000  # в минутах
                enemy.spd *= (1 + time_scale * 0.1)  # +10% скорости за минуту
                enemy.max_hp *= (1 + time_scale * 0.2)  # +20% здоровья за минуту
                enemy.current_hp = enemy.max_hp

                self.spawn_count += 1
