import pygame as pg
from pygame.math import Vector2


class visual(pg.sprite.Sprite):

    def draw(self, screen):
        screen.blit(self.image, self.rect.center)

    def animation(self):
        ANIMATION_COOLDOWN = 100
        if pg.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pg.time.get_ticks()
            self.index = (self.index + 1) % len(self.images)
            self.image = self.set_image()
            self.flip = pg.mouse.get_pos()[0] <= self.rect.centerx
            if self.flip:
                self.image = pg.transform.flip(self.image, self.flip, False)

    def set_animation(self, act='idle'):
        self.images = self.list[act]

    def set_image(self):
        return pg.transform.scale(pg.image.load(self.images[self.index]), self.scale)

    def set_sprites(self, list, scale, pos):
        self.scale = scale
        self.flip = False
        self.update_time = pg.time.get_ticks()
        self.list = list
        self.index = 0
        self.set_animation()
        self.image = self.set_image()
        self.rect = self.image.get_rect()
        self.rect.center = pos
