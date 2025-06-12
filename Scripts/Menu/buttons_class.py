import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, screen, x_percent, y_percent, width_percent, height_percent,
                 text, image_path, hover_image_path=None, sound_path=None):
        super().__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        #размер, позиция текста и кнопки
        self.width = int(self.screen_rect.width * width_percent)
        self.height = int(self.screen_rect.height * height_percent)
        self.x = int(self.screen_rect.width * x_percent)
        self.y = int(self.screen_rect.height * y_percent)
        self.text = text
        self.font = pygame.font.Font("Assets\Alagard-12px-unicode.otf", int(self.height * 0.6))
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect(center=(self.width // 2, self.height // 2))
        #отображение кнопки
        self.normal_image = pygame.image.load(image_path).convert_alpha()
        self.normal_image = pygame.transform.scale(self.normal_image, (self.width, self.height))

        if hover_image_path:
            self.hover_image = pygame.image.load(hover_image_path).convert_alpha()
            self.hover_image = pygame.transform.scale(self.hover_image, (self.width, self.height))
        else:
            self.hover_image = self.normal_image

        self.image = self.normal_image
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.is_hovered = False
    #отображение что курсор наведен на кнопку
    def update(self):
        if self.is_hovered:
            self.image = self.hover_image
        else:
            self.image = self.normal_image
    #проверка что курсор наведен на кнопку
    def check_hover(self, mouse_pos):
        was_hovered = self.is_hovered
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        self.image.blit(self.text_surface, self.text_rect)
        if was_hovered != self.is_hovered:
            self.update()
    #взаимодействие с кнопкой
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
