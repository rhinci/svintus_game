import pygame as pg
from pygame.math import Vector2


class visual(pg.sprite.Sprite):

    def draw(self, screen):
        screen.blit(self.image,self.rect.center)


    def set_sprites(self, images,scale,pos):
        self.animation_list = list()
        self.flip = False
        self.index = 0
        self.update_time = pg.time.get_ticks()
        for i in range (len(images)):
            img = pg.image.load(images[i])
            img = pg.transform.scale(img,scale)
            self.animation_list.append(img)
        self.image = self.animation_list[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = pos
