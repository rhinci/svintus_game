from .playermove import PlayerMove
from .visual import visual
from .specifications import specifications
import pygame as pg


class Player(PlayerMove, visual, specifications):
    def __init__(self,all_sprites,player_group, atk, spd_atk, spd, max_hp, pos, scale):
        super().__init__(all_sprites,player_group)
        self.set_stats(atk, spd_atk, spd, max_hp, 'Player')
        self.scale = scale
        self.pos = pos
        self.weapon = None
        self.shoot_cooldown = 0

        self.images =["Scripts\Game\General\Assets\Animations\Player_idle\Player-0000.png",
                      "Scripts\Game\General\Assets\Animations\Player_idle\Player-0001.png",
                      "Scripts\Game\General\Assets\Animations\Player_idle\Player-0002.png",
                      "Scripts\Game\General\Assets\Animations\Player_idle\Player-0003.png"]
        self.pos = pg.Vector2(pos)
        self.set_sprites(self.images,self.scale,self.pos)

    def set_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        buttons = pg.mouse.get_pressed(num_buttons=3)
        if self.weapon != None:
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
        ANIMATION_COOLDOWN = 100
        if pg.time.get_ticks()-self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pg.time.get_ticks()
            self.index = (self.index+1)%len(self.animation_list)
            self.image = self.animation_list[self.index]
            self.flip = pg.mouse.get_pos()[0] <= self.rect.centerx
            if self.flip:
                self.image = pg.transform.flip(self.image,self.flip,False)
        self.rect.center = self.pos
        self.weapon.rect.center = self.rect.center
