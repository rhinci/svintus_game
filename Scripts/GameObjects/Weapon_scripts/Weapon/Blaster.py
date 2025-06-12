from Scripts.GameObjects.Weapon_scripts.Projectiles.LaserProjectile import laserprojectile
from Scripts.GameObjects.Weapon_scripts.Weapon.Weapon import weapon
import pygame as pg

class blaster(weapon):
    #атака
    def fire(self, pos):
        if pg.time.get_ticks() - self.cooldown >= self.spd_atk:
            self.cooldown = pg.time.get_ticks()
            laserprojectile(self.all_sprites, self.target, self.mob_group,
                            self.rect.center, pos, self.projectile)
