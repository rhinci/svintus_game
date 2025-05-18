import pygame
import math


class bullet(pygame.sprite.Sprite):
    def __init__(self, all_sprites, targets, mob_group, start_pos, confiq):
        super().__init__(all_sprites)
        # Вычисляем угол и направление

        dy = pygame.mouse.get_pos()[1] - start_pos[1]
        dx = pygame.mouse.get_pos()[0] - start_pos[0]
        self.angle = math.atan2(dy, dx)
        self.image = pygame.transform.scale(pygame.image.load(confiq['image']), confiq['scale'])  # Красная пуля
        self.rect = self.image.get_rect(center=start_pos)
        self.image = pygame.transform.rotate(self.image, 90 + math.degrees(self.angle))

        self.all_sprites = all_sprites
        self.targets = targets
        self.mob_group = mob_group
        # Скорость пули
        self.speed = confiq['spd']
        self.dmg = confiq['dmg']
        # Устанавливаем начальную скорость
        self.velocity = (self.speed * math.cos(self.angle), self.speed * math.sin(self.angle))

    def projectile_collision(self):
        # Удаляем пулю, если она вышла за экран
        if self.rect.x < 0 or self.rect.x > pygame.display.get_surface().get_width() or \
                self.rect.y < 0 or self.rect.y > pygame.display.get_surface().get_height():
            self.kill()

        if pygame.sprite.spritecollideany(self, self.targets):
            hit_targets = [h_t for h_t in self.targets if self.rect.colliderect(h_t.rect)]
            for hit_target in hit_targets:
                if pygame.sprite.collide_mask(self, hit_target):
                    if hit_target.is_alive():
                        hit_target.change_hp(-self.dmg)
                        self.kill()

    def update(self):
        # Обновляем позицию пули
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        self.projectile_collision()
