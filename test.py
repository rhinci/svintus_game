import pygame as pg
from Scripts.Game.General import Player
from Scripts.Game.General import Bullet
from Scripts.Game.General import Weapon
from Scripts.Game.General import Enemy
from Scripts.Game.General import Spawner
from Scripts.Game.General.configs.character_config import PLAYER
from Scripts.Game.General.configs.enemy_config import MELEE_ENEMY
from Scripts.Game.General.configs.weapon_config import WEAPON
pg.init()
clock = pg.time.Clock()
#дисплей
size = (2200,1080)
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
FPS = 60
#группы
all_sprites = pg.sprite.Group()
weapon_group = pg.sprite.Group()
enemy_group = pg.sprite.Group()
player_group = pg.sprite.Group()

#оружие
#Игрок0
pos = (size[0]/2,size[1]/2)
player = Player.Player(all_sprites,player_group,PLAYER,pos)
weapon = Weapon.Weapon(all_sprites,enemy_group,weapon_group,WEAPON)
weapon.set_sprite_size((50,50))
player.set_weapon(weapon)
#враги
spawner = Spawner.spawner(all_sprites,enemy_group,player,1,size)
bullets = pg.sprite.Group()
running = True
while running:
    clock.tick(FPS)
    screen.fill((0,0,0))
    all_sprites.draw(screen)
    player_group.draw(screen)
    all_sprites.update()

    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.K_ESCAPE:
            running = False
            break
    spawner.update()
    pg.display.flip()
