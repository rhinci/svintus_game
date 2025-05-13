import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, screen, x_percent, y_percent, width_percent, height_percent,
                 text, image_path, hover_image_path=None, sound_path=None):
        super().__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width = int(self.screen_rect.width * width_percent)
        self.height = int(self.screen_rect.height * height_percent)
        self.x = int(self.screen_rect.width * x_percent)
        self.y = int(self.screen_rect.height * y_percent)
        self.text = text

        self.normal_image = pygame.image.load(image_path).convert_alpha()
        self.normal_image = pygame.transform.scale(self.normal_image, (self.width, self.height))

        if hover_image_path:
            self.hover_image = pygame.image.load(hover_image_path).convert_alpha()
            self.hover_image = pygame.transform.scale(self.hover_image, (self.width, self.height))
        else:
            self.hover_image = self.normal_image

        self.image = self.normal_image
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.sound = pygame.mixer.Sound(sound_path) if sound_path else None
        self.is_hovered = False

    def update(self):
        if self.is_hovered:
            self.image = self.hover_image
        else:
            self.image = self.normal_image

        if self.text:
            img_copy = self.image.copy()
            font = pygame.font.Font(None, int(self.height * 0.6))
            text_surface = font.render(self.text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(self.width // 2, self.height // 2))
            img_copy.blit(text_surface, text_rect)
            self.image = img_copy

    def check_hover(self, mouse_pos):
        was_hovered = self.is_hovered
        self.is_hovered = self.rect.collidepoint(mouse_pos)

        if was_hovered != self.is_hovered:
            self.update()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))