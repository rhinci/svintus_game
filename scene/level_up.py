import pygame as pg
from configs.screen_config import SIZE,WIDTH,HEIGHT
from Scripts.Menu.buttons_class import Button
from Scripts.Menu.background_anim import Background
from configs.btns_config import BUFF_BUTTON_DEFINITIONS

def level_up_scene(time):
    # инициализация основных систем
    clock = pg.time.Clock()
    FPS = 60
    screen = pg.display.set_mode(SIZE)
    time = pg.time.get_ticks()
    background = Background()
    #инициализация кнопок
    buff_buttons = pg.sprite.Group()
    button_instances = {}

    for btn_def in BUFF_BUTTON_DEFINITIONS:
        btn = Button(screen, btn_def["x_pos"], btn_def["y_pos"], btn_def["width"], btn_def["height"], btn_def["text"], btn_def["image"], btn_def["hover_image"])
        buff_buttons.add(btn)
        button_instances[btn_def["name"]] = btn

    while True:
        clock.tick(FPS)
        #отображение кнопок
        background.draw(screen)
        buff_buttons.draw(screen)
        #взаимодействия с кнопками
        for event in pg.event.get():
            #наведение на кнопку
            if event.type == pg.MOUSEMOTION:
                for button in buff_buttons:
                    button.check_hover(event.pos)
            #нажатие
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                for button in buff_buttons:
                    if button.is_hovered:
                        if button == button_instances["BuffAtk"]:
                            return 0, pg.time.get_ticks() - time
                        elif button == button_instances["BuffHP"]:
                            return 1, pg.time.get_ticks() - time
                        elif button == button_instances["BuffSPD"]:
                            return 2, pg.time.get_ticks() - time
        pg.display.flip()
