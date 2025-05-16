import pygame as pg
import random as r
class spawner():
    def __init__(self,list_of_enemys):
        self.screen = pg.display.get_surface()
        self.list_of_enemys = list_of_enemys
        self.update_time = pg.time.get_ticks()
    def spawn(self,mob):
        mob
        x = r.randint(200,int(self.screen.get_size()[0]/2))
        y = r.randint(200,int(self.screen.get_size()[1]/2))
        pos = (x,y)
        mob.pos = pos
    def update(self):
        ANIMATION_COOLDOWN = 100
        if pg.time.get_ticks()-self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pg.time.get_ticks()
            self.spawn(self.list_of_enemys[r.randint(0,len(self.list_of_enemys)-1)])
