import pygame as pg
from Scripts.Game.General.Player import Player
from Scripts.Game.Weapon_scripts.Mashinegun import mashineGun
from Scripts.Game.Weapon_scripts.RocketLauncher import rocketlauncher
from Scripts.Game.Weapon_scripts.LaserGun import lasergun
from Scripts.Game.General import Spawner
from configs.character_config import PLAYER
from configs.weapon_config import MASHINEGUN, LASERGUN, ROCKETLAUNCHER
from configs.screen_config import SIZE, HEIGHT, WIDTH
from Scripts.Menu.canvas_class import Interface
from configs.music import MUSIC

def easy_scene(num):
    # инициализация основных систем
    pg.init()
    pg.mixer.init()

    clock = pg.time.Clock()
    FPS = 60
    screen = pg.display.set_mode(SIZE)
    interface = Interface()
    pg.mixer.music.load(MUSIC['musicgame'])
    pg.mixer.music.play(-1)
    running = True
    paused = False

    # группы
    all_sprites = pg.sprite.Group()
    weapon_group = pg.sprite.Group()
    player_group = pg.sprite.Group()
    enemy_group = pg.sprite.Group()
    mobs_group = pg.sprite.Group()

    # игрок
    pos = (WIDTH / 2, HEIGHT / 2)
    player = Player(all_sprites, player_group, mobs_group, PLAYER, pos)
    match num:
        case 0:
            player.set_weapon(mashineGun(all_sprites, mobs_group, enemy_group, weapon_group, MASHINEGUN, player.pos))
        case 1:
            player.set_weapon(rocketlauncher(all_sprites, mobs_group, enemy_group, weapon_group, ROCKETLAUNCHER, player.pos))
        case 2:
            player.set_weapon(lasergun(all_sprites, mobs_group, enemy_group, weapon_group, LASERGUN, pos))
    # враги
    spawner = Spawner.spawner(all_sprites, enemy_group, mobs_group, player, 1, SIZE)
    player.curr_hp = 50

    while running:
        clock.tick(FPS)
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        spawner.update()
        interface.draw_button(screen, "", (255, 0, 0), 0, HEIGHT - 50, WIDTH, 50)
        interface.draw_button(screen, "", (0, 255, 0), 0, HEIGHT - 50, WIDTH * player.curr_hp / player.max_hp, 50)
        interface.draw_button(screen, "", (0, 183, 235), 0, HEIGHT - 75, WIDTH * player.EXP / 50, 25)
        interface.draw_text(screen, "HP", WIDTH / 2, HEIGHT - 50)
        interface.draw_text(screen, "EXP", WIDTH / 2, HEIGHT - 75)
        interface.draw_text(screen, "ATK:{0}".format(player.weapon.projectile['dmg']), 100, 150)
        interface.draw_text(screen, "{0} min: {1} sec".format(pg.time.get_ticks() // 36000, (pg.time.get_ticks() // 600) % 60), WIDTH / 2, 20)

        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.mixer.music.unload()
                running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    paused = not paused


                    if event.key == pg.K_1:
                        player.change_weapon(mashineGun(all_sprites, mobs_group, enemy_group, weapon_group, MASHINEGUN, player.pos))
                    if event.key == pg.K_2:
                        player.change_weapon(rocketlauncher(all_sprites, mobs_group, enemy_group, weapon_group, ROCKETLAUNCHER, player.pos))
                    if event.key == pg.K_3:
                        player.change_weapon(lasergun(all_sprites, mobs_group, enemy_group, weapon_group, LASERGUN, pos))

        pg.display.flip()
