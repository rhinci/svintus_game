import pygame
from Scripts.Game.Weapon_scripts.Projectiles.Bullet import bullet


class laserbeam(bullet):
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
