import pygame
import sys

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Цвета
WHITE = (255, 255, 255)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprites = self.load_sprites()
        self.current_frame = 0
        self.frame_count = len(self.sprites)
        self.animation_speed = 0.1  # Скорость анимации
        self.animation_timer = 0

    def load_sprites(self):
        sprite_sheet = pygame.image.load('Scripts\Game\General\Assets\Animations\Player_idle').convert_alpha()  # Загрузка спрайт-листа
        # Предполагается, что спрайты 64x64 пикселя
        frame_rects = [pygame.Rect(i * 64, 0, 64, 64) for i in range(3)]  # 3 кадра анимации
        return [sprite_sheet.subsurface(rect) for rect in frame_rects]

    def update(self, dt):
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % self.frame_count

    def draw(self, surface):
        surface.blit(self.sprites[self.current_frame], (self.x, self.y))

# Главная функция игры
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Player Animation Example')
        self.clock = pygame.time.Clock()
        self.player = Player(100, 100)

    def run(self):
        while True:
            dt = self.clock.tick(FPS) / 1000  # Время в секундах
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Обновление игрока
            self.player.update(dt)

            # Отрисовка
            self.screen.fill(WHITE)
            self.player.draw(self.screen)
            pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.run()
