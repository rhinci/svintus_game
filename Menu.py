import pygame as pg
import sys
from Scripts.Menu.buttons_class import Button
from Scripts.Menu.background_anim import Background
from configs.screen_config import SIZE, HEIGHT, WIDTH
from configs.btns_config import MENU_BUTTON_DEFINITIONS
from configs.music import MUSIC
from PLAY import game_scene
from credits import credits_scene
from weapon_choice import weapon_scene

def main_menu():
    pg.init()
    #основные системы
    pg.mixer.init()
    screen = pg.display.set_mode(SIZE)
    pg.display.set_caption("Rusostrus")
    pg.mixer.music.load(MUSIC['musicmenu'])
    pg.mixer.music.play(-1)
    pg.mixer.music.set_volume(0.01)
    font_size = int(HEIGHT * 0.1)
    pixel_font = pg.font.Font("Assets\Alagard-12px-unicode.otf", font_size)
    #фон
    background = Background()
    index = 0
    #инициализация кнопок
    buttons = pg.sprite.Group()
    button_instances = {}
    for btn_def in MENU_BUTTON_DEFINITIONS:
        btn = Button(screen, btn_def["x_pos"], btn_def["y_pos"], btn_def["width"], btn_def["height"], btn_def["text"],btn_def["image"], btn_def["hover_image"])
        buttons.add(btn)
        button_instances[btn_def["name"]] = btn

    running = True
    while running:
        background.draw(screen)
        text_surface = pixel_font.render("RUSOSTRUS", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 6))
        screen.blit(text_surface, text_rect)
        #взаимодействие с кнопками
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
            if event.type == pg.USEREVENT:
                if event.button == button_instances["easy"]:
                    pg.mixer.music.unload()
                    game_scene(index)
                    pg.mixer.music.load(MUSIC['musicmenu'])
                    pg.mixer.music.play(-1)
                    pg.mixer.music.set_volume(0.01)
                elif event.button == button_instances["weapon"]:
                    index = weapon_scene(index)
                elif event.button == button_instances["credits"]:
                    credits_scene()
                elif event.button == button_instances["exit"]:
                    print("Exiting game")
                    pg.quit()
                    sys.exit()
            for btn in button_instances.values():
                btn.handle_event(event)
        mouse_pos = pg.mouse.get_pos()
        for btn in button_instances.values():
            btn.check_hover(mouse_pos)

        buttons.draw(screen)
        pg.display.flip()
