import pygame
from configs.interface_config import INTERFACE
class Interface:
    def __init__(self, stats = INTERFACE):
        self.width = stats['width']
        self.height = stats['height']
        self.background_color = (30, 30, 30)
        self.text_color = (100, 100, 255)
        self.font_size = stats['font_size']
        self.font = pygame.font.Font(stats['font_name'], self.font_size)

    def draw_background(self, screen):
        screen.fill(self.background_color)

    def draw_text(self, screen, text, x, y):
        text_surface = self.font.render(text, True, self.text_color)
        screen.blit(text_surface, (x, y))

    def draw_button(self, screen, text, x, y, width, height):
        button_color = (100, 100, 100)
        pygame.draw.rect(screen, button_color, (x, y, width, height))
        self.draw_text(screen, text, x + 10, y + 10)
