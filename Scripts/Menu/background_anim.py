import pygame as pg
from configs.screen_config import BACKGROUND_DATA
class Background:
    def __init__(self, data = BACKGROUND_DATA):
        self.images = data['anim']
        self.size = data['size']
        self.index = 0
        self.update_time = 100

    def draw(self,screen):
        self.animation()
        screen.blit(pg.transform.scale(pg.image.load(self.images[self.index]).convert(),self.size),(0,0))

    #анимация
    def animation(self):
        ANIMATION_COOLDOWN = 500
        if pg.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pg.time.get_ticks()
            self.index = (self.index + 1) % len(self.images)
