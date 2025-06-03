from Scripts.Game.Weapon_scripts.Weapon import weapon
from Scripts.Game.Weapon_scripts.Projectiles.Fire import fire
from configs.projectiles_config import FIRE
import pygame as pg
class firethrower(weapon):
    def fire(self,pos):
        fire(self.all_sprites,self.target,self.mob_group,self.rect.center,pos,FIRE)
