import pygame


class Button:
    def __init__(self, screen, x_percent, y_percent, width_percent, height_percent,
                 text, image_path, hover_image_path=None, sound_path=None):

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width = int(self.screen_rect.width * width_percent)
        self.height = int(self.screen_rect.height * height_percent)

        self.x = int(self.screen_rect.width * x_percent)
        self.y = int(self.screen_rect.height * y_percent)
        self.text = text

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        if hover_image_path:
            self.hover_image = pygame.image.load(hover_image_path).convert_alpha()
            self.hover_image = pygame.transform.scale(self.hover_image, (self.width, self.height))
        else:
            self.hover_image = self.image

        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.sound = pygame.mixer.Sound(sound_path) if sound_path else None
        self.is_hovered = False

    def draw(self):
        current_image = self.hover_image if self.is_hovered else self.image
        self.screen.blit(current_image, self.rect.topleft)

        if self.text:
            font = pygame.font.Font(None, int(self.height * 0.6))
            text_surface = font.render(self.text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=self.rect.center)
            self.screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
