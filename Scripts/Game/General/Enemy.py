import pygame as pg
from .specifications import specifications
from .visual import visual


class Enemy(specifications, visual):
    def __init__(self, atk, spd_atk, spd, max_hp, size, screen, pos):
        super().__init__()
        self.set_stats(atk, spd_atk, spd, max_hp, 'Enemy')
        self.size = size
        self.screen = screen
        self.set_sprite('Scripts\Game\General\Assets\Enemy.png', pos)
        self.set_sprite_size(self.size)
        self.pos = pos

    def update(self):
        self.sprite_move(self.screen, self.pos)

    def death(self):
        return super().death()
