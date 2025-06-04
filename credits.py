import pygame as pg
from configs.screen_config import SIZE, HEIGHT, WIDTH


def credits_scene():
    pg.init()

    clock = pg.time.Clock()
    FPS = 60
    screen = pg.display.set_mode(SIZE)
    running = True

    title_font = pg.font.Font("Assets/GNF.ttf", int(HEIGHT * 0.06))
    text_font = pg.font.Font("Assets/GNF.ttf", int(HEIGHT * 0.035))
    small_font = pg.font.Font("Assets/GNF.ttf", int(HEIGHT * 0.025))

    while running:
        clock.tick(FPS)
        screen.fill((0, 0, 0))

        title_text = title_font.render("Svintus Games Production", True, (255, 255, 255))
        text1 = text_font.render("Gromyko Ilya", True, (255, 255, 255))
        text2 = text_font.render("Lupanova Daria", True, (255, 255, 255))
        text3 = text_font.render("Simonenko Egor", True, (255, 255, 255))
        hint_text = small_font.render("Press ESC to return to the main menu", True, (150, 150, 150))

        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT * 0.18))
        screen.blit(text1, (WIDTH // 2 - text1.get_width() // 2, HEIGHT * 0.4))
        screen.blit(text2, (WIDTH // 2 - text2.get_width() // 2, HEIGHT * 0.5))
        screen.blit(text3, (WIDTH // 2 - text3.get_width() // 2, HEIGHT * 0.6))
        screen.blit(hint_text, (WIDTH // 2 - hint_text.get_width() // 2, HEIGHT * 0.8))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return "exit"

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return "main_menu"

        pg.display.flip()
