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
from Scripts.Menu.canvas_class import Interface
def easy_scene(num):
    #инициализация основных систем
    pg.init()
    clock = pg.time.Clock()
    FPS = 60
    screen = pg.display.set_mode(SIZE)
    interface = Interface()
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
    match num:
        case 0:
            player.set_weapon(mashineGun(all_sprites,mobs_group,enemy_group,weapon_group,MASHINEGUN,player.pos))
        case 1:
            player.set_weapon(rocketlauncher(all_sprites,mobs_group,enemy_group,weapon_group,ROCKETLAUNCHER,player.pos))
        case 2:
            player.set_weapon(lasergun(all_sprites,mobs_group,enemy_group,weapon_group,LASERGUN,pos))
    #враги
    spawner = Spawner.spawner(all_sprites,enemy_group,mobs_group,player,1,SIZE)

    while running:
        clock.tick(FPS)
        screen.fill((0,0,0))
        all_sprites.draw(screen)
        all_sprites.update()
        spawner.update()
        interface.draw_text(screen,"HP:{0}%".format(100*player.curr_hp/player.max_hp),100,50)
        interface.draw_text(screen,"EXP:{0}".format(player.EXP),100,100)
        interface.draw_text(screen,"ATK:{0}".format(player.weapon.projectile['dmg']),100,150)
        interface.draw_text(screen,"{0} min: {1} sec".format(pg.time.get_ticks()//36000,(pg.time.get_ticks()//600)%60),WIDTH/2,20)
        for event in pg.event.get():
            if (event.type == pg.QUIT or
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE or
                pg.time.get_ticks()//36000 == 10 and (pg.time.get_ticks()//600)%60 == 0):
                running = False
        pg.display.flip()
    pg.quit()
