from .playermove import PlayerMove
from .visual import visual
from .specifications import specifications
import pygame as pg


class Player(PlayerMove, visual, specifications):
    def __init__(self, atk, spd_atk, spd, max_hp, pos, scale, screen):
        self.set_stats(atk, spd_atk, spd, max_hp, 'Player')
        self.scale = scale
        self.screen = screen
        self.pos = pos
        self.weapon = None
        self.shoot_cooldown = 0
        self.set_sprite("Scripts\Game\General\Assets\Player.png", pos)
        self.set_sprite_size(self.scale)

    def set_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        buttons = pg.mouse.get_pressed(num_buttons=3)
        if buttons[0] and self.shoot_cooldown == 0:
            self.weapon.fire()
            self.shoot_cooldown = 50

    def update(self):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= self.spd_atk
        if self.shoot_cooldown < 0:
            self.shoot_cooldown = 0
        self.attack()
        self.pos = self.move(self.pos, self.spd, self.scale)
        self.rect.center = self.pos
        self.rotate()
        self.sprite_move(self.screen)
        self.weapon.draw(self.screen, self.rect.center)
