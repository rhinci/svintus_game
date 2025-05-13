import pygame as pg
from pygame.math import Vector2


class visual(pg.sprite.Sprite):

    def sprite_move(self, screen):
        screen.blit(self.image, self.rect)

    def set_sprite(self, image, pos):
        self.image = pg.image.load(image)
        self.orig_image = self.image
        self.rect = self.image.get_rect(center=pos)
        self.pos = Vector2(pos)

    def rotate(self):
        flipped = pg.mouse.get_pos()[0] <= self.rect.centerx
        self.image = pg.transform.flip(self.orig_image, flipped, False)
        self.rect = self.image.get_rect(center=self.rect.center)

    def set_sprite_size(self, scale):
        self.orig_image = pg.transform.scale(self.orig_image, scale)
