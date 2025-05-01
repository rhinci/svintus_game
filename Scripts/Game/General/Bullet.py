import pygame
import math
class Bullet(pygame.sprite.Sprite):
    def __init__(self, start_pos,spd,dmg):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 0, 0))  # Красная пуля
        self.rect = self.image.get_rect(center=start_pos)
        # Вычисляем угол и направление
        mouse_pos = pygame.mouse.get_pos()
        dx = mouse_pos[0] - start_pos[0]
        dy = mouse_pos[1] - start_pos[1]
        self.angle = math.atan2(dy, dx)

        # Скорость пули
        self.speed = spd
        self.dmg = dmg

        # Устанавливаем начальную скорость
        self.velocity = (self.speed*math.cos(self.angle), self.speed*math.sin(self.angle))

    def collision_with_enemy(self,enemy_group):
        enemies_hit = pygame.sprite.spritecollide(self,enemy_group,False)
        for enemy in enemies_hit:
            enemy.change_hp(-self.dmg)
            self.kill()

    def update(self):
        # Обновляем позицию пули
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        # Удаляем пулю, если она вышла за экран
        if self.rect.x < 0 or self.rect.x > pygame.display.get_surface().get_width() or \
           self.rect.y < 0 or self.rect.y > pygame.display.get_surface().get_height():
            self.kill()
