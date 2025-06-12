import pygame
from configs.interface_config import INTERFACE


class Interface:
    def __init__(self, stats=INTERFACE):
        self.width = stats['width']
        self.height = stats['height']
        self.background_color = (30, 30, 30)
        self.text_color = (105, 54, 43)
        self.font_size = stats['font_size']
        self.font = pygame.font.Font(stats['font_name'], self.font_size)

    def draw_background(self, screen):
        screen.fill(self.background_color)

    def draw_text(self, screen, text, x, y, color = None):
        if color == None:
            color = self.text_color
        text_surface = self.font.render(text, True, color)
        screen.blit(text_surface, (x, y))

    def draw_button(self, screen, text, color, x, y, width, height):
        pygame.draw.rect(screen, color, (x, y, width, height))
        self.draw_text(screen, text, x + 10, y + 10)
