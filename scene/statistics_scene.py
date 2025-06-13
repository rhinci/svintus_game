import pygame as pg
from configs.screen_config import SIZE, HEIGHT, WIDTH


def achievements_scene(player_stats):
    pg.init()

    clock = pg.time.Clock()
    FPS = 60
    screen = pg.display.set_mode(SIZE)
    running = True

    title_font = pg.font.Font("Assets/GNF.ttf", int(HEIGHT * 0.06))
    text_font = pg.font.Font("Assets/GNF.ttf", int(HEIGHT * 0.035))
    hint_font = pg.font.Font("Assets/GNF.ttf", int(HEIGHT * 0.035))

    default_stats = {
        "1. Kills": 0,  #
        "2. Time played": 0,  #
        "3. Crystals collected": 0,  #
        "4. Damage taken": 0,  #
        "5. Damage dealt": 0,  #
        "6. Bullets used": 0,  #
    }
    stats = player_stats if player_stats else default_stats
    #отображение статистики
    while running:
        clock.tick(FPS)
        screen.fill((0, 0, 0))

        title = title_font.render("Achievements", True, (255, 215, 0))
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT * 0.15))

        y_offset = HEIGHT * 0.3
        for i, (key, value) in enumerate(stats.items()):
            if i % 2 == 0:
                pg.draw.rect(screen, (50, 50, 60), (WIDTH * 0.2, y_offset - 5, WIDTH * 0.6, HEIGHT * 0.06))

            key_text = text_font.render(key, True, (220, 220, 220))
            screen.blit(key_text, (WIDTH * 0.25, y_offset))

            value_text = text_font.render(str(int(value)), True, (255, 255, 150))
            screen.blit(value_text, (WIDTH * 0.75 - value_text.get_width(), y_offset))

            y_offset += HEIGHT * 0.07

        hint = hint_font.render("Press ESC to return to the main menu", True, (150, 150, 180))
        screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, HEIGHT * 0.9))
    #выход из статистики
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return "exit"

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return "main_menu"

        pg.display.flip()
