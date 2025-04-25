import pygame
import sys
from buttons_class import Button

pygame.init()

WIDTH, HEIGHT = 1080, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rusostrus")

easy_btn = Button(screen, 0.35, 0.3, 0.3, 0.1, "", "assets/btn_easy.png", "assets/btn_easy_hovered.png")
hard_btn = Button(screen, 0.35, 0.45, 0.3, 0.1, "", "assets/btn_hard.png", "assets/btn_hard_hovered.png")
exit_btn = Button(screen, 0.35, 0.6, 0.3, 0.1, "", "assets/btn_exit.png", "assets/btn_exit_hovered.png")


def main_menu():
    running = True
    while running:
        screen.fill((168, 181, 178))

        font_size = int(HEIGHT * 0.1)
        pixel_font = pygame.font.Font("General/assets/Lover-unity.otf", font_size)

        text_surface = pixel_font.render("Rusostrus", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 6))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT:
                if event.button == easy_btn:
                    print("Easy mode selected")
                    # точка входа в изи мод

                elif event.button == hard_btn:
                    print("Hard mode selected")
                    # точка входа в хард мод | установка флага для модификаторов скейлинга

                elif event.button == exit_btn:
                    print("Exiting game")
                    pygame.quit()
                    sys.exit()

            easy_btn.handle_event(event)
            hard_btn.handle_event(event)
            exit_btn.handle_event(event)

        mouse_pos = pygame.mouse.get_pos()
        easy_btn.check_hover(mouse_pos)
        hard_btn.check_hover(mouse_pos)
        exit_btn.check_hover(mouse_pos)

        easy_btn.draw()
        hard_btn.draw()
        exit_btn.draw()

        pygame.display.flip()


main_menu()
