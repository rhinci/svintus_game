import pygame as pg
from Scripts.Game.General.Player import Player
from Scripts.Game.Weapon_scripts.Mashinegun import mashineGun
from Scripts.Game.Weapon_scripts.RocketLauncher import rocketlauncher
from Scripts.Game.Weapon_scripts.Mashinegun import mashineGun
from Scripts.Game.Weapon_scripts.LaserGun import lasergun
from Scripts.Game.General import Spawner
from configs.character_config import PLAYER
from configs.weapon_config import MASHINEGUN,LASERGUN,ROCKETLAUNCHER
from configs.screen_config import SIZE,HEIGHT,WIDTH

#инициализация основных систем
pg.init()
clock = pg.time.Clock()
FPS = 60
screen = pg.display.set_mode(SIZE)
running = True

#группы
all_sprites = pg.sprite.Group()
weapon_group = pg.sprite.Group()
player_group = pg.sprite.Group()
enemy_group = pg.sprite.Group()
mobs_group = pg.sprite.Group()

#игрок
pos = (WIDTH/2,HEIGHT/2)
player = Player(all_sprites,player_group,mobs_group,PLAYER,pos)
mashineGun_ = lasergun(all_sprites,mobs_group,enemy_group,weapon_group,LASERGUN,player.pos)
player.set_weapon(mashineGun_)

#враги
spawner = Spawner.spawner(all_sprites,enemy_group,mobs_group,player,1,SIZE)

while running:
    clock.tick(FPS)
    screen.fill((0,0,0))
    all_sprites.draw(screen)
    all_sprites.update()
    spawner.update()
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                player.change_weapon(mashineGun(all_sprites,mobs_group,enemy_group,weapon_group,MASHINEGUN,player.pos))
            if event.key == pg.K_2:
                player.change_weapon(rocketlauncher(all_sprites,mobs_group,enemy_group,weapon_group,ROCKETLAUNCHER,player.pos))
    pg.display.flip()
pg.quit()
