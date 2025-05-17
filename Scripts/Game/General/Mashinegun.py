from Scripts.Game.General.Bullet import Bullet
from Scripts.Game.General.Weapon import Weapon
from Scripts.Game.General.configs.projectiles_config import BULLET
class mashineGun(Weapon):
    def fire(self):
        Bullet(self.all_sprites,self.target,self.mob_group,
                   self.rect.center,
                    BULLET)
