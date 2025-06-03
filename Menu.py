import pygame
import sys

import pygame.mixer_music
from Scripts.Menu.buttons_class import Button
from configs.screen_config import SIZE, HEIGHT, WIDTH
from configs.btns_config import MENU_BUTTON_DEFINITIONS
from configs.music import MUSIC
from easy_mode import easy_scene
from hard_mode import hard_scene
from credits import credits_scene


def main_menu():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Rusostrus")
    pygame.mixer.music.load(MUSIC['musicmenu'])
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    background = pygame.image.load("Assets\_UIMenu\Background.png").convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    index = 0
    buttons = pygame.sprite.Group()
    button_instances = {}

    for btn_def in MENU_BUTTON_DEFINITIONS:
        btn = Button(screen, btn_def["x_pos"], btn_def["y_pos"], btn_def["width"], btn_def["height"], "",
                     btn_def["image"], btn_def["hover_image"])
        buttons.add(btn)
        button_instances[btn_def["name"]] = btn

    running = True
    while running:
        screen.blit(background, (0, 0))

        font_size = int(HEIGHT * 0.1)
        pixel_font = pygame.font.Font("Assets/GNF.ttf", font_size)
        text_surface = pixel_font.render("Rusostrus", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 6))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT:
                if event.button == button_instances["easy"]:
                    pygame.mixer.music.unload()
                    easy_scene(index)
                    pygame.mixer.music.load(MUSIC['musicmenu'])
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.5)

                elif event.button == button_instances["hard"]:
                    pygame.mixer.music.unload()
                    hard_scene(index)
                    pygame.mixer.music.load(MUSIC['musicmenu'])
                    pygame.mixer.music.play(-1)

                elif event.button == button_instances["weapon"]:
                    index = (index + 1) % 5

                elif event.button == button_instances["credits"]:
                    pygame.mixer.music.unload()
                    credits_scene()
                    pygame.mixer.music.load(MUSIC['musicmenu'])
                    pygame.mixer.music.play(-1)

                elif event.button == button_instances["exit"]:
                    print("Exiting game")
                    pygame.quit()
                    sys.exit()

            for btn in button_instances.values():
                btn.handle_event(event)

        mouse_pos = pygame.mouse.get_pos()
        for btn in button_instances.values():
            btn.check_hover(mouse_pos)

        buttons.draw(screen)

        pygame.display.flip()
