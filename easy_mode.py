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
from Scripts.Menu.buttons_class import Button
from configs.pause_btns_config import PAUSE_BUTTON_DEFINITIONS


def easy_scene(num):
    # инициализация основных систем
    pg.init()
    clock = pg.time.Clock()
    FPS = 60
    screen = pg.display.set_mode(SIZE)
    interface = Interface()
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

    pause_buttons = pg.sprite.Group()
    button_instances = {}

    for btn_def in PAUSE_BUTTON_DEFINITIONS:
        btn = Button(screen, 0.35, btn_def["y_pos"], 0.3, 0.1, "", btn_def["image"], btn_def["hover_image"])
        pause_buttons.add(btn)
        button_instances[btn_def["name"]] = btn

    while running:
        clock.tick(FPS)
        screen.fill((0, 0, 0))
        if not paused:
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

        else:
            s = pg.Surface(SIZE, pg.SRCALPHA)
            s.fill((0, 0, 0))
            screen.blit(s, (0, 0))

            pause_buttons.draw(screen)

        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    paused = not paused

                if not paused:
                    if event.key == pg.K_1:
                        player.change_weapon(mashineGun(all_sprites, mobs_group, enemy_group, weapon_group, MASHINEGUN, player.pos))
                    if event.key == pg.K_2:
                        player.change_weapon(rocketlauncher(all_sprites, mobs_group, enemy_group, weapon_group, ROCKETLAUNCHER, player.pos))
                    if event.key == pg.K_3:
                        player.change_weapon(lasergun(all_sprites, mobs_group, enemy_group, weapon_group, LASERGUN, pos))

            # Обработка кнопок паузы
            if paused:
                if event.type == pg.MOUSEMOTION:
                    for button in pause_buttons:
                        button.check_hover(event.pos)

                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    for button in pause_buttons:
                        if button.is_hovered:
                            if button == button_instances["resume"]:
                                paused = False
                            elif button == button_instances["main_menu"]:
                                pg.quit()
                                return "main_menu" # нужно переходить в меню
                            elif button == button_instances["exit"]:
                                running = False

        pg.display.flip()
    pg.quit()
