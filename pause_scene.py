import pygame as pg
import sys
from configs.screen_config import SIZE
from Scripts.Menu.buttons_class import Button
from configs.btns_config import PAUSE_BUTTON_DEFINITIONS
from configs.screen_config import SIZE

def pause(time):
    # инициализация основных систем
    clock = pg.time.Clock()
    FPS = 60
    screen = pg.display.set_mode(SIZE)
    time = pg.time.get_ticks()
    background = pg.transform.scale(pg.image.load("Assets\_UIMenu\Background.png").convert(), SIZE)
    #кнопки
    pause_buttons = pg.sprite.Group()
    button_instances = {}
    for btn_def in PAUSE_BUTTON_DEFINITIONS:
        btn = Button(screen, 0.35, btn_def["y_pos"], 0.3, 0.1, btn_def["text"], btn_def["image"], btn_def["hover_image"])
        pause_buttons.add(btn)
        button_instances[btn_def["name"]] = btn

    while True:
        clock.tick(FPS)
        screen.blit(background, (0, 0))

        pause_buttons.draw(screen)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p or event.key == pg.K_ESCAPE:
                    return True, pg.time.get_ticks()-time
            # Обработка кнопок паузы
            if event.type == pg.MOUSEMOTION:
                for button in pause_buttons:
                    button.check_hover(event.pos)
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                for button in pause_buttons:
                    if button.is_hovered:
                        if button == button_instances["resume"]:
                            return True, pg.time.get_ticks() - time
                        elif button == button_instances["main_menu"]:
                            return False, pg.time.get_ticks() - time
                        elif button == button_instances["exit"]:
                            pg.quit()
                            sys.exit()

        pg.display.flip()
