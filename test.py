from Scripts.Game import Player as p
import pygame as pg

pg.init()

height = 1000
width = 1000
screen_size = (width,height)
screen = pg.display.set_mode(screen_size)

player = p.Player()
player.set_stats(1,1,0.1,1)
x,y = height//2,width//2
player.set_sprite("Scripts\Game\General\Assets\PlayerImage.jpg",(x,y))
size = (100,100)
player.set_sprite_size(size)

run = True
while run:
    screen.fill((0,0,0))
    player.rotate()
    player.sprite_move(screen,(x,y))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    keys = pg.key.get_pressed()
    x,y = player.move(x,y,player.spd,keys,screen_size,size)
    pg.display.flip()
pg.quit()
