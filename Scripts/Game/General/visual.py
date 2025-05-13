import pygame as pg
from pygame.math import Vector2


class visual(pg.sprite.Sprite):

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.change_sprite(self)

    def change_sprite(self):
        self.index = (self.index + 1)%len(self.images)
        self.image = self.images[self.index]
        self.orig_image = self.image
        self.set_sprite_size(self.scale)


    def set_sprite(self, images, pos,scale):
        self.images = images
        self.index = 0
        self.image = self.images[self.index]
        self.scale = scale
        self.orig_image = self.image
        self.rect = self.image.get_rect(center=pos)

    def rotate(self):
        flipped = pg.mouse.get_pos()[0] <= self.rect.centerx
        self.image = pg.transform.flip(self.orig_image, flipped, False)
        self.rect = self.image.get_rect(center=self.rect.center)

    def set_sprite_size(self):
        self.orig_image = pg.transform.scale(self.orig_image, self.scale)
