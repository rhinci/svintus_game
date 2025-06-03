from Scripts.Game.Weapon_scripts.Projectiles.Rocket import Rocket
from Scripts.Game.Weapon_scripts.Weapon import weapon


class rocketlauncher(weapon):
    def fire(self,pos):
        Rocket(self.all_sprites, self.target, self.mob_group, self.rect.center,pos, self.projectile)
