from Scripts.Game.Weapon_scripts.Projectiles.LaserProjectile import laserprojectile
from Scripts.Game.Weapon_scripts.Weapon import weapon
import pygame as pg


class lasergun(weapon):
    def fire(self):
        if pg.time.get_ticks() - self.cooldown >= self.spd_atk:
            self.cooldown = pg.time.get_ticks()
            laserprojectile(self.all_sprites, self.target, self.mob_group,
                   self.rect.center, self.projectile)
