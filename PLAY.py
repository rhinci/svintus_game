import pygame as pg
from Scripts.Game.General.Player import Player
from Scripts.Game.Weapon_scripts.Mashinegun import mashineGun
from Scripts.Game.Weapon_scripts.RocketLauncher import rocketlauncher
from Scripts.Game.Weapon_scripts.Blaster import blaster
from Scripts.Game.Weapon_scripts.FireThrower import firethrower
from Scripts.Game.Weapon_scripts.LaserGun import lasergun
from Scripts.Game.General import Spawner
from configs.character_config import PLAYER
from configs.weapon_config import MASHINEGUN, BLASTER, ROCKETLAUNCHER, FIRETHROWER, LASERGUN
from configs.screen_config import SIZE, HEIGHT, WIDTH
from Scripts.Menu.canvas_class import Interface
from configs.music import MUSIC
from Scripts.Game.General.statistics_collector import run_stats
from pause_scene import pause
from level_up import level_up_scene

def game_scene(index):
    # инициализация основных систем
    pg.init()
    pg.mixer.init()
    run_stats.reset_stats()
    run_stats.start_run()
    clock = pg.time.Clock()
    FPS = 60
    screen = pg.display.set_mode(SIZE,pg.DOUBLEBUF)
    interface = Interface()
    running = True
    pg.mixer.music.load(MUSIC['musicgame'])
    pg.mixer.music.play(-1)
    pg.mixer.music.set_volume(0.01)
    timer = 0
    background = pg.transform.scale(pg.image.load("Assets\_UIGame\Background.png").convert(),SIZE)

    # группы
    all_sprites = pg.sprite.Group()
    weapon_group = pg.sprite.Group()
    player_group = pg.sprite.Group()
    enemy_group = pg.sprite.Group()
    mobs_group = pg.sprite.Group()

    # игрок
    pos = (WIDTH / 2, HEIGHT / 2)
    player = Player(all_sprites, player_group, mobs_group, PLAYER, pos)
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

    # враги
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
        interface.draw_button(screen, "", (255, 0, 0), 0, HEIGHT - 50, WIDTH, 50)
        interface.draw_button(screen, "", (0, 255, 0), 0, HEIGHT - 50, WIDTH * player.curr_hp / player.max_hp, 50)
        interface.draw_button(screen, "", (0, 183, 235), 0, HEIGHT - 75, WIDTH * player.EXP / 50, 25)
        interface.draw_text(screen, "HP", WIDTH / 2, HEIGHT - 50)
        interface.draw_text(screen, "EXP", WIDTH / 2, HEIGHT - 75)
        interface.draw_text(screen, "ATK:{0}".format(player.weapon.projectile['dmg']), 100, 150)
        interface.draw_text(screen, "{0} min: {1} sec".format((pg.time.get_ticks() - timer) // 36000,((pg.time.get_ticks() - timer) // 600) % 60),WIDTH / 2, 20)

        if (player.EXP % 50 == 0 and player.EXP != 0):
            player.EXP = 0
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
