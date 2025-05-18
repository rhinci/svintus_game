from Scripts.Game.Weapon_scripts.Projectiles.Rocket import Rocket
from Scripts.Game.Weapon_scripts.Weapon import weapon
from configs.projectiles_config import ROCKET
class rocketlauncher(weapon):
    def fire(self):
        Rocket(self.all_sprites,self.target,self.mob_group,self.rect.center,ROCKET)
