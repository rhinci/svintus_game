import pygame as pg
import random as r
<<<<<<< HEAD
from Scripts.Game.General.Enemies.Melee_enemy import melee_enemy
from Scripts.Game.General.Enemies.Range_enemy import range_enemy
from configs.enemy_config import MELEE_ENEMY, RANGE_ENEMY
from Scripts.Game.Weapon_scripts.Mashinegun import mashineGun
from Scripts.Game.Weapon_scripts.RocketLauncher import rocketlauncher
from Scripts.Game.Weapon_scripts.Blaster import blaster
from Scripts.Game.Weapon_scripts.FireThrower import firethrower
from Scripts.Game.Weapon_scripts.LaserGun import lasergun
from configs.enemy_weapon_config import MASHINEGUN, BLASTER, ROCKETLAUNCHER, FIRETHROWER, LASERGUN

list_of_enemys = [MELEE_ENEMY, RANGE_ENEMY]
=======
from Scripts.Game.General.Enemy import enemy, melee_enemy
from configs.enemy_config import MELEE_ENEMY
list_of_enemys = [MELEE_ENEMY]
>>>>>>> a864d326e757da45ddd8d1284cf0dcf62177f364

class spawner():
<<<<<<< HEAD
    def __init__(self, all_sprites, enemy_group, mob_group,weapon_group, player,player_group, spawn_cooldown, screen):
        self.spawn_cooldown = spawn_cooldown * 1000
=======
    def __init__(self,all_sprites,enemy_group,mob_group,player,spawn_cooldown,screen):
        self.spawn_cooldown = spawn_cooldown*1000
>>>>>>> a864d326e757da45ddd8d1284cf0dcf62177f364
        self.all_sprites = all_sprites
        self.enemy_group = enemy_group
        self.mob_group = mob_group
        self.weapon_group = weapon_group
        self.player_group = player_group
        self.target = player
        self.screen = screen
        self.list_of_enemys = list_of_enemys
        self.update_time = pg.time.get_ticks()
    def spawn(self):
        x = r.randint(0,int(self.screen[0]))
        y = r.randint(0,int(self.screen[1]))
        pos = (x,y)
        return pos
<<<<<<< HEAD

    def random_weapon(self,pos):
        chance = r.randint(0,100)
        if 0<= chance <25:
            weapon = mashineGun(self.all_sprites, self.mob_group, self.player_group, self.weapon_group, MASHINEGUN, pos)
        elif chance == 25:
            weapon = rocketlauncher(self.all_sprites, self.mob_group, self.player_group, self.weapon_group, ROCKETLAUNCHER, pos)
        elif 26<= chance < 75:
            weapon = firethrower(self.all_sprites,self.mob_group,self.player_group,self.weapon_group, FIRETHROWER,pos)
        else:
            weapon = blaster(self.all_sprites,self.mob_group,self.player_group,self.weapon_group, BLASTER, pos)

        return weapon


    def update(self):
        if pg.time.get_ticks() - self.update_time >= self.spawn_cooldown and len(self.enemy_group) <=20:
            self.update_time = pg.time.get_ticks()
            pos = self.spawn()
            enemy = r.choice(list_of_enemys)
            if enemy == MELEE_ENEMY:
                melee_enemy(self.all_sprites, self.enemy_group, self.mob_group, self.target, MELEE_ENEMY,
                                pos)
            elif enemy == RANGE_ENEMY:
                    range_enemy(self.all_sprites, self.enemy_group, self.mob_group, self.target, MELEE_ENEMY,
                                self.spawn(),self.random_weapon(pos))
=======
    def update(self):
        if pg.time.get_ticks()-self.update_time >= self.spawn_cooldown:
            self.update_time = pg.time.get_ticks()
            match r.choice(list_of_enemys):
                case MELEE_ENEMY:
                    melee_enemy(self.all_sprites,self.enemy_group,self.mob_group,self.target,MELEE_ENEMY,self.spawn())
>>>>>>> a864d326e757da45ddd8d1284cf0dcf62177f364
