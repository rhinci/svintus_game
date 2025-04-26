import pygame as pg
from math import atan2,pi
from pygame.math import Vector2
class visual(pg.sprite.Sprite):

    def sprite_move(self,screen,pos):
        screen.blit(self.image,pos)

    def set_sprite(self, image,pos):
        self.image = pg.image.load(image)
        self.orig_image = self.image
        self.rect = self.image.get_rect(center = pos)
        self.pos = Vector2(pos)
    def update(self):
        self.rotate()
    def rotate(self):
        direction = pg.mouse.get_pos()-self.pos
        angle = direction.as_polar()[1]
        self.image = pg.transform.rotate(self.orig_image,-angle)
        self.rect = self.image.get_rect(center = self.rect.center)
    def set_sprite_size(self,size):
        self.orig_image = pg.transform.scale(self.orig_image,size)
