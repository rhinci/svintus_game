import pygame as pg
from Scripts.Game.General import Player
from Scripts.Game.General import Bullet
from Scripts.Game.General import Weapon

pg.init()
clock = pg.time.Clock()
#дисплей
size = (1080,900)
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
FPS = 60
#оружие
#Игрок
pos = (size[0]/2,size[1]/2)
weapon = Weapon.Weapon("Scripts\Game\General\Assets\pngwing.com.png",10,10,pos)
weapon.set_sprite_size((100,50))
player = Player.Player(1,1,10,1,pos,(200,200),screen)
player.set_weapon(weapon)

bullets = pg.sprite.Group()

running = True

while running:
    clock.tick(FPS)
    screen.fill((0,0,0))
    player.update()
    player.weapon.bullets.update()
    player.weapon.bullets.draw(screen)

    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.K_ESCAPE:
            running = False
            break

    pg.display.flip()
