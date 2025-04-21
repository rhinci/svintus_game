import pygame as pg

class visual(pg.sprite.Sprite):
    def set_sprite(self,image,x,y):
        self.image = pg.image.load(image)
        self.rect = self.image.get_rect(x,y)

    def set_sprite_size(self,new_size):
        self.image = pg.transform.scale(self.image,new_size)
