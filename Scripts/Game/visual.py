import pygame as pg


class visual(pg.sprite.Sprite):
    def set_sprite(self, image):
        self.image = pg.image.load(image)

    def sprite_move(self,screen,pos):
        screen.blit(self.image,pos)

    def set_sprite_size(self, new_size):
        self.image = pg.transform.scale(self.image, new_size)
