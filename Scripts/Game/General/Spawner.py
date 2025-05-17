import pygame as pg
import random as r
from Scripts.Game.General.Enemy import enemy,melee_enemy
from configs.enemy_config import MELEE_ENEMY
list_of_enemys = [MELEE_ENEMY]

class spawner():
    def __init__(self,all_sprites,enemy_group,mob_group,player,spawn_cooldown,screen):
        self.spawn_cooldown = spawn_cooldown*1000
        self.all_sprites = all_sprites
        self.enemy_group = enemy_group
        self.mob_group = mob_group
        self.target = player
        self.screen = screen
        self.list_of_enemys = list_of_enemys
        self.update_time = pg.time.get_ticks()
    def spawn(self):
        x = r.randint(0,int(self.screen[0]))
        y = r.randint(0,int(self.screen[1]))
        pos = (x,y)
        return pos
    def update(self):
        if pg.time.get_ticks()-self.update_time >= self.spawn_cooldown:
            self.update_time = pg.time.get_ticks()
            match r.choice(list_of_enemys):
                case MELEE_ENEMY:
                    melee_enemy(self.all_sprites,self.enemy_group,self.mob_group,self.target,MELEE_ENEMY,self.spawn())
