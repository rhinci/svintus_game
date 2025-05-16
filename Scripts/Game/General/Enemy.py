import pygame as pg
from .specifications import specifications
from .visual import visual
from .Explosion import explosion
import math
class enemy(specifications, visual):
    def __init__(self,all_sprites,enemy_group,player, stats, pos):
        super().__init__(all_sprites,enemy_group)
        self.set_stats(stats)
        self.all_sprites = all_sprites
        self.enemy_group = enemy_group
        self.images = stats['images']
        self.scale = stats['scale']
        self.set_sprites(self.images,self.scale,pos)
        self.player = player
        self.rect.center = pos
        self.screen = pg.display.get_surface()
        self.weapon = None
        self.atk_cd = pg.time.get_ticks()

    def death(self):
        explosion(self.all_sprites,self.rect.center,self.scale)
        self.kill()

    def move(self):
        dx = self.player.pos[0] - self.rect.center[0]
        dy = self.player.pos[1] - self.rect.center[1]
        self.angle = math.atan2(dy, dx)
        self.velocity = (self.spd * math.cos(self.angle), self.spd * math.sin(self.angle))
    def border(self):
        if self.rect.centerx < self.scale[0]/2:
            self.rect.centerx = self.scale[0]/2
        if self.rect.centery < self.scale[0]/2:
            self.rect.centery = self.scale[0]/2
        if self.rect.centerx > self.screen.get_size()[0] - self.scale[0] / 2:
            self.rect.centerx = self.screen.get_size()[0] - self.scale[0] / 2
        if self.rect.centery > self.screen.get_size()[1] - self.scale[1] / 2:
            self.rect.centery = self.screen.get_size()[1] - self.scale[1] / 2

    def attack(self):
        pass

    def update(self):
        self.move()
        self.border()
        # Обновляем позицию врага
        if self.is_alive():
            if pg.sprite.spritecollideany(self,self.all_sprites):
                hit_targets = [h_t for h_t in self.targets if self.rect.colliderect(h_t.rect)]
                for hit_target in hit_targets:
                    if pg.sprite.collide_mask(self,hit_target):
                        if hit_target.is_alive():
                            if hit_target == self.player:
                                self.attack()
                            else:
                                self.rect.x-=self.velocity[0]
                                self.rect.y-=self.velocity[1]
            else:
                self.rect.x += self.velocity[0]
                self.rect.y += self.velocity[1]
class melee_enemy(enemy):
    def attack(self):
        if pg.time.get_ticks() - self.atk_cd >= 1000*self.spd_atk:
            self.cd = pg.time.get_ticks()
            self.player.change_hp(-self.atk)
    def update(self):
        self.move()
        self.border()
        # Обновляем позицию врага
        if self.is_alive():
            if self.rect.colliderect(self.player.rect):
                self.attack()
            else:
                self.rect.x += self.velocity[0]
                self.rect.y += self.velocity[1]
