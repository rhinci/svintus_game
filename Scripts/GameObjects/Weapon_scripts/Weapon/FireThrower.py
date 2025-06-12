from Scripts.GameObjects.Weapon_scripts.Weapon.Weapon import weapon
from Scripts.GameObjects.Weapon_scripts.Projectiles.Fire import fire
from configs.projectiles_config import FIRE


class firethrower(weapon):
    def fire(self, pos):
        fire(self.all_sprites, self.target, self.mob_group, self.rect.center, pos, FIRE)
