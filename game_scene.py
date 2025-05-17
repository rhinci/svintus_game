import pygame as pg
from Scripts.Game.General import Player
from Scripts.Game.General import Bullet
from Scripts.Game.General import Weapon
from Scripts.Game.General import Enemy
from Scripts.Game.General import Spawner
from Scripts.Game.General.configs.character_config import PLAYER
from Scripts.Game.General.configs.enemy_config import MELEE_ENEMY
from Scripts.Game.General.configs.weapon_config import WEAPON
from Scripts.Game.General.configs.screen_config import SIZE,HEIGHT,WIDTH

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
player = Player.Player(all_sprites,player_group,mobs_group,PLAYER,pos)
weapon = Weapon.Weapon(all_sprites,enemy_group,weapon_group,WEAPON)
player.set_weapon(weapon)

#враги
spawner = Spawner.spawner(all_sprites,enemy_group,mobs_group,player,1,SIZE)

while running:
    clock.tick(FPS)
    screen.fill((0,0,0))
    all_sprites.draw(screen)
    all_sprites.update()
    spawner.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.type == pg.K_SPACE:
                print('выход')
                running = False
    pg.display.flip()
pg.quit()
