from Scripts.Game.Rocket import Rocket
from Scripts.Game.General.Weapon import Weapon
from configs.projectiles_config import ROCKET
class rocketlauncher(Weapon):
    def fire(self):
        Rocket(self.all_sprites,self.target,self.mob_group,self.rect.center,ROCKET)
