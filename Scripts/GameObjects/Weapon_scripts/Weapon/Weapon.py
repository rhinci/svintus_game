import pygame as pg
from pygame.math import Vector2


class weapon(pg.sprite.Sprite):
    def __init__(self, all_sprites, mob_group, target_group, weapon_group, data, pos=(0, 0)):
    #инициализация основных переменных класса оружия
        super().__init__(all_sprites, weapon_group)
        self.image = pg.image.load(data['image'])
        self.orig_image = self.image
        self.rect = self.image.get_rect(center=pos)
        self.rect.center = pos
        self.spd_atk = data['atk_spd']
        self.cooldown = pg.time.get_ticks()
        self.projectile = data['projectile']
        self.all_sprites = all_sprites
        self.mob_group = mob_group
        self.bullet_group = pg.sprite.Group
        self.target = target_group
        self.sound = pg.mixer.Sound(data['sound'])
        self.sound.set_volume(0.1)
        self.weapon_chanel = pg.mixer.Channel(data['channel'])
        self.set_sprite_size(data['size'])
    #поворот оружия в сторону курсора
    def rotate(self, pos):
        direction = pos - Vector2(self.rect.midright)
        angle = -direction.as_polar()[1]
        flipped = pos[0] <= self.rect.centerx
        self.image = pg.transform.rotate(pg.transform.flip(self.orig_image, False, flipped), angle)
        self.rect = self.image.get_rect(center=self.rect.center)
    #изменение размера оружия
    def set_sprite_size(self, scale):
        self.orig_image = pg.transform.scale(self.orig_image, scale)
    #атака оружия
    def fire(self, pos):
        pass
    #отрисовка
    def draw(self, screen):
        screen.blit(self.image, self.image.get_size())
