import pygame as pg
from Scripts.Game.General.MobsScripts.specifications import specifications
from .MobsScripts.visual import visual
from Scripts.Game.Weapon_scripts.Explosion import explosion
from Scripts.Game.General.ItemBox import health_pack, exp_pack
from configs.collectables import HEALTH_PACK, EXP
import math
from random import randint
class enemy(specifications, visual):
    def __init__(self, all_sprites, enemy_group, mob_group, player, stats, pos):
        self.set_stats(stats)
        self.all_sprites = all_sprites
        self.all_sprites.add(self)
        self.enemy_group = enemy_group
        self.enemy_group.add(self)
        self.mob_group = mob_group
        self.mob_group.add(self)
        self.scale = stats['scale']
        self.images = stats['animation']
        self.set_sprites(self.images, self.scale, pos)
        self.player = player
        self.rect.center = pos
        self.screen = pg.display.get_surface()
        self.weapon = None
        self.atk_cd = pg.time.get_ticks()
        self.alive = True  # Добавляем флаг жив/мертв
    def move(self):
        dx = self.player.pos[0] - self.rect.center[0]
        dy = self.player.pos[1] - self.rect.center[1]
        self.angle = math.atan2(dy, dx)
        self.velocity = [self.spd * math.cos(self.angle), self.spd * math.sin(self.angle)]
    def death(self):
        match randint(1, 2):
            case 1:
                health_pack(self.all_sprites, HEALTH_PACK, self.player, self.rect.center)
            case 2:
                exp_pack(self.all_sprites, EXP, self.player, self.rect.center)

        explosion(self.all_sprites, self.mob_group, self.rect.center, (100, 100))
        self.kill()  # Удаляем из всех групп
        self.alive = False  # Помечаем как мертвого
        # Дополнительная очистка (опционально)
        self.all_sprites.remove(self)
        self.enemy_group.remove(self)
        self.mob_group.remove(self)

    def animation(self):
        ANIMATION_COOLDOWN = 300
        if pg.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pg.time.get_ticks()
            self.index = (self.index + 1) % len(self.images)
            self.image = self.set_image()
            self.image = pg.transform.flip(self.image, self.player.rect.centerx >= self.rect.centerx, False)

    def is_alive(self):
        return self.alive and self.curr_hp > 0  # Проверяем и флаг, и HP
    def attack(self):
        pass
    def border(self):
        if self.rect.centerx < self.scale[0] / 2:
            self.rect.centerx = self.scale[0] / 2
        if self.rect.centery < self.scale[0] / 2:
            self.rect.centery = self.scale[0] / 2
        if self.rect.centerx > self.screen.get_size()[0] - self.scale[0] / 2:
            self.rect.centerx = self.screen.get_size()[0] - self.scale[0] / 2
        if self.rect.centery > self.screen.get_size()[1] - self.scale[1] / 2:
            self.rect.centery = self.screen.get_size()[1] - self.scale[1] / 2
    def collision(self):
        if pg.sprite.spritecollideany(self, self.mob_group):
            collideds = [c for c in self.mob_group if c != self and self.rect.colliderect(c.rect) and c.is_alive()]
            for collided in collideds:
                if pg.sprite.collide_mask(self, collided):
                    if collided != self.player:
                        self.rect.x  -= self.velocity[0]
                        self.rect.y -= self.velocity[1]
                    else:
                        self.rect.x -= self.velocity[0]
                        self.rect.y -= self.velocity[1]
                        self.attack()

    def update(self):
        if not self.is_alive():
            return  # Не обновляем мертвых врагов

        self.move()
        self.border()
        self.animation()
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        self.collision()

        # Автоматическая проверка смерти
        if self.curr_hp <= 0 and self.alive:
            self.death()


class melee_enemy(enemy):
    def attack(self):
        if pg.time.get_ticks() - self.atk_cd >= 100 * self.spd_atk:
            self.atk_cd = pg.time.get_ticks()
            self.player.change_hp(-self.atk)
