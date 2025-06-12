import pygame as pg
from Scripts.GameObjects.PlayerScripts.specifications import specifications
from Scripts.GameObjects.PlayerScripts.visual import visual
from Scripts.GameObjects.Weapon_scripts.Weapon.Explosion import explosion
from Scripts.GameObjects.Other.ItemBox import health_pack, exp_pack
from configs.collectables import HEALTH_PACK, EXP
from Scripts.GameObjects.PlayerScripts.statistics_collector import run_stats
import math
from random import randint


class enemy(specifications, visual):
    def __init__(self, all_sprites, enemy_group, mob_group, player, stats, pos):
        self.screen = pg.display.get_surface()
        #установка статов и врага
        self.set_stats(stats)
        self.weapon = None
        self.atk_cd = pg.time.get_ticks()
        self.player = player
        self.alive = True  # Добавляем флаг жив/мертв
        #добавление в группы
        self.all_sprites = all_sprites
        self.all_sprites.add(self)
        self.enemy_group = enemy_group
        self.enemy_group.add(self)
        self.mob_group = mob_group
        self.mob_group.add(self)
        #настройки изображения и анимаций
        self.scale = stats['scale']
        self.images = stats['animation']
        self.set_sprites(self.images, self.scale, pos)
        #настройка начальной позиции и направления движения к игроку
        self.rect.center = pos
        self.player = player
        dx = self.player.pos[0] - self.rect.center[0]
        dy = self.player.pos[1] - self.rect.center[1]
        self.angle = math.atan2(dy, dx)
        self.velocity = [self.spd * math.cos(self.angle), self.spd * math.sin(self.angle)]

    def move(self):
        #бег в направлении игрока
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        dx = self.player.pos[0] - self.rect.center[0]
        dy = self.player.pos[1] - self.rect.center[1]
        self.angle = math.atan2(dy, dx)
        self.velocity = [self.spd * math.cos(self.angle), self.spd * math.sin(self.angle)]

    def death(self):
        #при смерти дроп хп и EXP
        chance = randint(0, 100)
        if 0 <= chance <= 25:
            health_pack(self.all_sprites, HEALTH_PACK, self.player, self.rect.center)
        elif 25 < chance <= 50:
            exp_pack(self.all_sprites, EXP, self.player, self.rect.center)
        #удаление врага с добавлением убийств
        explosion(self.all_sprites, self.mob_group, self.rect.center, (100, 100))
        self.kill()
        run_stats.increment_stat("1. Kills", 1)# Удаляем из всех групп
        self.alive = False  # Помечаем как мертвого
        # Дополнительная очистка
        self.all_sprites.remove(self)
        self.enemy_group.remove(self)
        self.mob_group.remove(self)

    def animation(self):
        #анимации
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
                        self.rect.x -= self.velocity[0]
                        self.rect.y -= self.velocity[1]
                    else:
                        self.rect.x -= 1.5*self.velocity[0]
                        self.rect.y -= 1.5*self.velocity[1]
                        self.attack()

    def update(self):
        if not self.is_alive():
            return  # Не обновляем мертвых врагов

        self.move()
        self.border()
        self.animation()

        self.collision()

        # Автоматическая проверка смерти
        if self.curr_hp <= 0 and self.alive:
            self.death()
