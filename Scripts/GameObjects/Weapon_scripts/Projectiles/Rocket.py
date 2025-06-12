import pygame
from Scripts.GameObjects.Weapon_scripts.Weapon.Explosion import explosion
from Scripts.GameObjects.Weapon_scripts.Projectiles.Bullet import bullet


class Rocket(bullet):
    def projectile_collision(self):
        if self.rect.x < 0 or self.rect.x > pygame.display.get_surface().get_width() or \
                self.rect.y < 0 or self.rect.y > pygame.display.get_surface().get_height():
            self.kill()
        if pygame.sprite.spritecollideany(self, self.targets):
            hit_targets = [h_t for h_t in self.targets if self.rect.colliderect(h_t.rect)]
            for hit_target in hit_targets:
                if pygame.sprite.collide_mask(self, hit_target):
                    if hit_target.is_alive():
                        explosion(self.all_sprites, self.mob_group, self.rect.center, (300, 300), 100)
                        self.kill()
