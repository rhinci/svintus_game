import pygame as pg
from Scripts.Game.General import Player
from Scripts.Game.General import Bullet
from Scripts.Game.General import Weapon
from Scripts.Game.General import Enemy

pg.init()
clock = pg.time.Clock()
#дисплей
size = (1200,1080)
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
FPS = 60

#группы
all_sprites = pg.sprite.Group()
player_group = pg.sprite.Group()
enemy_group = pg.sprite.Group()
weapon_group = pg.sprite.Group()
#оружие

#враги

#Игрок0
pos = (size[0]/2,size[1]/2)
weapon = Weapon.Weapon("Scripts\Game\General\Assets\pngwing.com.png",10,10,pos,all_sprites,enemy_group,weapon_group)
weapon.set_sprite_size((100,50))
player = Player.Player(all_sprites,player_group,1,10,10,100,pos,(500,500))
player.set_weapon(weapon)

bullets = pg.sprite.Group()

running = True

while running:
    clock.tick(FPS)
    screen.fill((0,0,0))
    all_sprites.draw(screen)
    weapon_group.draw(screen)
    enemy_group.update()
    all_sprites.update()

    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.K_ESCAPE:
            running = False
            break

    pg.display.flip()
