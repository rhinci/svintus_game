from Scripts.Menu.canvas_class import Interface
from configs.screen_config import SIZE
import pygame
# Пример использования
def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    running = True

    interface = Interface()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        interface.draw_text(screen, "100 - 100", 100, 50)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
main()
