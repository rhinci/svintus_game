import pygame as pg
from .specifications import specifications
from .visual import visual
import math

class enemy(specifications, visual):
    def __init__(self,all_sprites,enemy_group,player, atk, spd_atk, spd, max_hp, scale, pos):
        super().__init__(all_sprites,enemy_group)
        self.set_stats(atk, spd_atk, spd, max_hp, 'Enemy')
        self.images = ["Scripts\Game\General\Assets\Enemy.png"]
        self.scale = scale
        self.set_sprites(self.images,self.scale,pos)
        self.player = player
        self.rect.center = pos
        self.screen = pg.display.get_surface()
        self.weapon = None

    def death(self):
        self.kill()

    def move(self):
        dx = self.player.pos[0] - self.rect.center[0]
        dy = self.player.pos[1] - self.rect.center[1]
        self.angle = math.atan2(dy, dx)
        self.velocity = (self.spd * math.cos(self.angle), self.spd * math.sin(self.angle))
    def update(self):
        self.move()
        # Обновляем позицию врага
        if not(self.rect.colliderect(self.player.rect)) and self.is_alive():
            self.player.change_hp(-self.atk)
            print(self.player.get_curr_hp())
            self.rect.x += self.velocity[0]
            self.rect.y += self.velocity[1]



        if self.rect.centerx < self.scale[0]/2:
            self.rect.centerx = self.scale[0]/2
        if self.rect.centery < self.scale[0]/2:
            self.rect.centery = self.scale[0]/2
        if self.rect.centerx > self.screen.get_size()[0] - self.scale[0] / 2:
            self.rect.centerx = self.screen.get_size()[0] - self.scale[0] / 2
        if self.rect.centery > self.screen.get_size()[1] - self.scale[1] / 2:
            self.rect.centery = self.screen.get_size()[1] - self.scale[1] / 2
