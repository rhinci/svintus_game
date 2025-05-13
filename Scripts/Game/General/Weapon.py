import pygame as pg
from .Bullet import Bullet
from pygame.math import Vector2


class Weapon():
    def __init__(self, image, spd, dmg, pos):
        self.image = pg.image.load(image)
        self.orig_image = self.image
        self.rect = self.image.get_rect(center=pos)
        self.pos = Vector2(pos)

        self.bullet_spd = spd
        self.bullet_dmg = dmg
        self.cooldown = 1
        self.bullets = pg.sprite.Group()

    def rotate(self):
        direction = pg.mouse.get_pos() - self.pos
        angle = -direction.as_polar()[1]
        flipped = pg.mouse.get_pos()[0] <= self.rect.centerx
        self.image = pg.transform.rotate(pg.transform.flip(self.orig_image, False, flipped), angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def set_sprite_size(self, scale):
        self.orig_image = pg.transform.scale(self.orig_image, scale)

    def fire(self):
        self.bullets.add(Bullet(self.rect.midright, self.bullet_spd, self.bullet_dmg))

    def draw(self, screen, pos):
        self.rect.center = pos
        self.rotate()
        screen.blit(self.image, pos)
