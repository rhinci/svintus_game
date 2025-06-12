from Scripts.GameObjects.Weapon_scripts.Projectiles.Bullet import bullet
from Scripts.GameObjects.Weapon_scripts.Weapon.Weapon import weapon

import pygame as pg


class mashineGun(weapon):
    #атака
    def fire(self, pos):
        if pg.time.get_ticks() - self.cooldown >= self.spd_atk:
            if not(self.weapon_chanel.get_busy()):
                self.sound.play()
            self.cooldown = pg.time.get_ticks()
            bullet(self.all_sprites, self.target, self.mob_group,
                   self.rect.center, pos, self.projectile)
