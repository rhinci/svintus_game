import pygame as pg
from Scripts.GameObjects.PlayerScripts.Player import Player
from Scripts.GameObjects.Weapon_scripts.Weapon.Mashinegun import mashineGun
from Scripts.GameObjects.Weapon_scripts.Weapon.RocketLauncher import rocketlauncher
from Scripts.GameObjects.Weapon_scripts.Weapon.Blaster import blaster
from Scripts.GameObjects.Weapon_scripts.Weapon.FireThrower import firethrower
from Scripts.GameObjects.Weapon_scripts.Weapon.LaserGun import lasergun
from Scripts.GameObjects.Other import Spawner
from configs.character_config import PLAYER
from configs.weapon_config import MASHINEGUN, BLASTER, ROCKETLAUNCHER, FIRETHROWER, LASERGUN
from configs.screen_config import SIZE, HEIGHT, WIDTH
from Scripts.Menu.canvas_class import Interface
from configs.music import MUSIC
from Scripts.GameObjects.PlayerScripts.statistics_collector import run_stats
from scene.pause_scene import pause
from scene.level_up import level_up_scene

def game_scene(index):
    # инициализация основных систем
    pg.init()
    pg.mixer.init()
    clock = pg.time.Clock()
    FPS = 60
    screen = pg.display.set_mode(SIZE,pg.DOUBLEBUF)
    interface = Interface()
    running = True
    pg.mixer.music.load(MUSIC['musicgame'])
    pg.mixer.music.play(-1)
    pg.mixer.music.set_volume(0.1)
    #таймер
    timer = 0
    #фон
    background = pg.transform.scale(pg.image.load("Assets\_UIGame\Background.png").convert(),SIZE)
    curr_hp = pg.transform.scale(pg.image.load("Assets\_UIGame\hp_full.png").convert(),(WIDTH,60))
    empty_hp = pg.transform.scale(pg.image.load("Assets\_UIGame\hp_empty.png").convert(),(WIDTH,60))
    empty_exp = pg.transform.scale(pg.image.load("Assets\_UIGame\exp_empty.png").convert(),(WIDTH,30))
    exp = pg.transform.scale(pg.image.load("Assets\_UIGame\exp.png").convert(),(WIDTH,30))
    timer_image = pg.transform.scale(pg.image.load("Assets\_UIGame\Timer2.png"),(300,100))
    #группы
    all_sprites = pg.sprite.Group()
    weapon_group = pg.sprite.Group()
    player_group = pg.sprite.Group()
    enemy_group = pg.sprite.Group()
    mobs_group = pg.sprite.Group()

    #игрок
    pos = (WIDTH / 2, HEIGHT / 2)
    player = Player(all_sprites, player_group, mobs_group, PLAYER, pos)
    run_stats.reset_stats()
    run_stats.start_run()
    num_to_upgrade = 5
    #установка оружия
    match index:
        case 0:
            player.set_weapon(mashineGun(all_sprites, mobs_group, enemy_group, weapon_group, MASHINEGUN, player.pos))
        case 1:
            player.set_weapon(
                rocketlauncher(all_sprites, mobs_group, enemy_group, weapon_group, ROCKETLAUNCHER, player.pos))
        case 2:
            player.set_weapon(blaster(all_sprites, mobs_group, enemy_group, weapon_group, BLASTER, player.pos))
        case 3:
            player.set_weapon(firethrower(all_sprites, mobs_group, enemy_group, weapon_group, FIRETHROWER, player.pos))
        case 4:
            player.set_weapon(lasergun(all_sprites, mobs_group, enemy_group, weapon_group, LASERGUN, player.pos))

    #враги
    spawner = Spawner.spawner(all_sprites, enemy_group, mobs_group, weapon_group, player, player_group, 1, SIZE)

    while running:
        clock.tick(FPS)
        screen.blit(background,(0,0))
        if not(player.is_alive()):
            break

        all_sprites.draw(screen)
        weapon_group.draw(screen)
        all_sprites.update()
        spawner.update()
        screen.blit(empty_hp,(0,HEIGHT-60))
        screen.blit(empty_exp,(0,HEIGHT-85))
        screen.blit(pg.transform.scale(curr_hp,(WIDTH*(player.curr_hp>=0)*player.curr_hp/player.max_hp, 60)),(0,HEIGHT-60))
        screen.blit(pg.transform.scale(exp,(WIDTH*player.EXP/num_to_upgrade, 25)), (0,HEIGHT-85))
        screen.blit(timer_image,(WIDTH/2-75,10))
        interface.draw_text(screen, "HP:{0}/{1}".format(int(player.curr_hp),player.max_hp), WIDTH / 2-60, HEIGHT - 50,(0,0,0))
        interface.draw_text(screen, "EXP:{0}/{1}".format(player.EXP,num_to_upgrade), WIDTH / 2-60, HEIGHT - 95,(0,0,0))
        interface.draw_text(screen, "{0} min: {1} sec".format((pg.time.get_ticks() - timer) // 36000,((pg.time.get_ticks() - timer) // 600) % 60),WIDTH / 2-20, 40,(0, 0, 0))

        if (player.EXP % num_to_upgrade == 0 and player.EXP != 0):
            player.EXP = 0
            num_to_upgrade += 5
            buff_index , time = level_up_scene(timer)
            timer += time
            player.buff(buff_index)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p or event.key == pg.K_ESCAPE:
                    running,time = pause(timer)
                    timer+=time
        pg.display.flip()
    run_stats.end_run()
    if player.is_alive():
        player.death()
    pg.mixer.music.unload()
