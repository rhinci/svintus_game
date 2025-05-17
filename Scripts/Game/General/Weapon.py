import pygame as pg
from .Bullet import Bullet
from pygame.math import Vector2
import math as m

class Weapon(pg.sprite.Sprite):
    def __init__(self, all_sprites,target_group,weapon_group,stats,pos = (0,0)):
        super().__init__(all_sprites,weapon_group)
        self.image = pg.image.load(stats['image'])
        self.orig_image = self.image
        self.rect = self.image.get_rect(center=pos)
        self.rect.center = pos
        self.bullet_spd = stats['spd']
        self.bullet_dmg = stats['dmg']
        self.cooldown = 1
        self.all_sprites = all_sprites
        self.bullet_group = pg.sprite.Group
        self.target = target_group
        self.set_sprite_size(stats['size'])
    def rotate(self):
        direction = pg.mouse.get_pos() - Vector2(self.rect.midright)
        angle = -direction.as_polar()[1]
        flipped = pg.mouse.get_pos()[0] <= self.rect.centerx
        self.image = pg.transform.rotate(pg.transform.flip(self.orig_image, False, flipped), angle)
        self.rect = self.image.get_rect(center=self.rect.center)
    def set_sprite_size(self, scale):
        self.orig_image = pg.transform.scale(self.orig_image, scale)
    def fire(self):
            Bullet(self.all_sprites,self.target,
                   self.rect.center,
                    self.bullet_spd, self.bullet_dmg)

    def update(self):
        self.rotate()
    def draw(self,screen):
        screen.blit(self.image,self.image.get_size())
