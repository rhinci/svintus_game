import pygame
import math
class Bullet(pygame.sprite.Sprite):
    def __init__(self,all_sprites,targets, start_pos, spd, dmg):
        super().__init__(all_sprites)
        # Вычисляем угол и направление


        dy = pygame.mouse.get_pos()[1] - start_pos[1]
        dx = pygame.mouse.get_pos()[0] - start_pos[0]
        self.angle = math.atan2(dy,dx)
        self.image = pygame.Surface((15,1))
        self.image.fill((255, 0, 0))  # Красная пуля
        self.rect = self.image.get_rect(center=start_pos)
        print(self.angle)
        self.image = pygame.transform.rotate(self.image,math.degrees(self.angle))


        self.targets = targets
        # Скорость пули
        self.speed = spd
        self.dmg = dmg
        # Устанавливаем начальную скорость
        self.velocity = (self.speed * math.cos(self.angle), self.speed * math.sin(self.angle))
    def update(self):
        # Обновляем позицию пули
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        # Удаляем пулю, если она вышла за экран
        if self.rect.x < 0 or self.rect.x > pygame.display.get_surface().get_width() or \
                self.rect.y < 0 or self.rect.y > pygame.display.get_surface().get_height():
            self.kill()

        if pygame.sprite.spritecollideany(self,self.targets):
            hit_targets = [h_t for h_t in self.targets if self.rect.colliderect(h_t.rect)]
            for hit_target in hit_targets:
                if pygame.sprite.collide_mask(self,hit_target):
                    if hit_target.is_alive():
                        hit_target.change_hp(-self.dmg)
                        self.kill()
