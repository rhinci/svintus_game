from Scripts.GameObjects.Weapon_scripts.Projectiles.Bullet import bullet
from Scripts.GameObjects.Weapon_scripts.Weapon.Weapon import weapon

class lasergun(weapon):
    #атака
    def fire(self, pos):
        if not(self.weapon_chanel.get_busy()):
                self.sound.play()
        bullet(self.all_sprites, self.target, self.mob_group,
               self.rect.midright, pos, self.projectile)
