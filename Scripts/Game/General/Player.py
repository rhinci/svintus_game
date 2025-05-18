from Scripts.Game.General.MobsScripts.playermove import PlayerMove
from Scripts.Game.General.MobsScripts.visual import visual
from Scripts.Game.General.MobsScripts.specifications import specifications
import pygame as pg
import sys
import math


class Player(PlayerMove, visual, specifications):
    def __init__(self, all_sprites, player_group, mob_group, stats, pos):
        super().__init__(all_sprites, player_group, mob_group)
        self.set_stats(stats)
        self.scale = stats['scale']
        self.pos = pos
        self.weapon = None
        self.shoot_cooldown = 0
        self.mob_group = mob_group
        self.images = stats["animation"]
        self.pos = pg.Vector2(pos)
        self.set_sprites(self.images, self.scale, self.pos)

    def set_weapon(self, weapon):
        self.weapon = weapon

    def change_weapon(self, weapon):
        self.weapon.kill()
        self.weapon = weapon
        self.shoot_cooldown = self.weapon.spd_atk

    def collision(self):
        if pg.sprite.spritecollideany(self, self.mob_group):
            collideds = [c for c in self.mob_group if c != self and self.rect.colliderect(c.rect) and c.is_alive()]
            for collided in collideds:
                if pg.sprite.collide_rect(self, collided):
                    dx = collided.rect.center[0] - self.rect.center[0]
                    dy = collided.rect.center[1] - self.rect.center[1]
                    angle = math.atan2(dy, dx)
                    self.rect.x -= self.rect.size[0] * math.cos(angle)
                    self.rect.y -= self.rect.size[1] * math.sin(angle)

    def death(self):
        pg.quit()
        sys.exit()

    def attack(self):
        buttons = pg.mouse.get_pressed(num_buttons=3)
        if self.weapon != None:
            if buttons[0] and self.shoot_cooldown == 0:
                self.weapon.fire()
                self.shoot_cooldown = self.spd_atk

    def player_move(self):
        if self.move_h() == 0 and self.move_v() == 0:
            self.set_animation()
        else:
            self.pos = self.move(self.pos, self.spd, self.scale)
            self.set_animation('run')
        self.animation()

    def buff_atk(self, atk):
        self.weapon.projectile['dmg'] += atk

    def update(self):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= self.weapon.spd_atk
        if self.shoot_cooldown < 0:
            self.shoot_cooldown = 0

        self.attack()
        self.player_move()
        self.rect.center = self.pos
        self.weapon.rect.center = self.rect.center

        if (self.EXP % 50 == 0 and self.EXP != 0):
            self.EXP = 0
            self.buff_atk(10)
