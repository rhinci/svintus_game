from Scripts.GameObjects.Weapon_scripts.Weapon.Weapon import weapon
from Scripts.GameObjects.Weapon_scripts.Projectiles.Fire import fire
from configs.projectiles_config import FIRE
import pygame as pg

class firethrower(weapon):
    #атака
    def fire(self, pos):
        if pg.time.get_ticks() - self.cooldown >= self.spd_atk:
            if not(self.weapon_chanel.get_busy()):
                self.sound.play()
            self.cooldown = pg.time.get_ticks()
            fire(self.all_sprites, self.target, self.mob_group, self.rect.center, pos, FIRE)
