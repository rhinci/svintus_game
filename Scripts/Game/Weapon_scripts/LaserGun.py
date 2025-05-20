from Scripts.Game.Weapon_scripts.Projectiles.Bullet import bullet
from Scripts.Game.Weapon_scripts.Weapon import weapon
import pygame as pg


class lasergun(weapon):
    def fire(self):

        bullet(self.all_sprites, self.target, self.mob_group,
                   self.rect.center, self.projectile)
