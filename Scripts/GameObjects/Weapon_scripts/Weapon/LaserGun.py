from Scripts.GameObjects.Weapon_scripts.Projectiles.Bullet import bullet
from Scripts.GameObjects.Weapon_scripts.Weapon.Weapon import weapon

class lasergun(weapon):
    def fire(self, pos):
        bullet(self.all_sprites, self.target, self.mob_group,
               self.rect.midright, pos, self.projectile)
