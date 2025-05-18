from Scripts.Game.Weapon_scripts.Projectiles.Bullet import bullet
from Scripts.Game.Weapon_scripts.Weapon import weapon
from configs.projectiles_config import BULLET
class mashineGun(weapon):
    def fire(self):
        bullet(self.all_sprites,self.target,self.mob_group,
                   self.rect.center,
                    BULLET)
