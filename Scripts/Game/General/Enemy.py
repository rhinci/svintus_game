import pygame as pg
from .specifications import specifications
from .visual import visual


class enemy(specifications, visual):
    def __init__(self,all_sprites,enemy_group, atk, spd_atk, spd, max_hp, size, screen, pos):
        super().__init__(all_sprites,enemy_group)
        self.set_stats(atk, spd_atk, spd, max_hp, 'Enemy')
        self.size = size
        self.screen = screen
        self.set_sprite('Scripts\Game\General\Assets\Enemy.png', pos)
        self.set_sprite_size(self.size)

    def update(self):
        self.kill()
