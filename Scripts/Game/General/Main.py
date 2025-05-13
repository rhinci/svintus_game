import pygame
import sys
from buttons_class import Button
from Scripts.Game.General.configs.btns_config import BUTTON_DEFINITIONS

pygame.init()

WIDTH, HEIGHT = 1080, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rusostrus")

background = pygame.image.load("Assets/Background.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


def main_menu():
    buttons = pygame.sprite.Group()
    button_instances = {}

    for btn_def in BUTTON_DEFINITIONS:
        btn = Button(screen, 0.35, btn_def["y_pos"], 0.3, 0.1, "", btn_def["image"], btn_def["hover_image"])
        buttons.add(btn)
        button_instances[btn_def["name"]] = btn

    running = True
    while running:
        screen.blit(background, (0, 0))

        font_size = int(HEIGHT * 0.1)
        pixel_font = pygame.font.Font("Assets/Lover-unity.otf", font_size)
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
                    print("Easy mode selected")
                    # точка входа в изи мод

                elif event.button == button_instances["hard"]:
                    print("Hard mode selected")
                    # точка входа в хард мод

                elif event.button == button_instances["weapon"]:
                    print("Open weapon selection")
                    # вход в меню выбора оружия

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


main_menu()
