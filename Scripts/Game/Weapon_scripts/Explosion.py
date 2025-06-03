import pygame as pg


class explosion(pg.sprite.Sprite):
    def __init__(self, all_sprites, targets, pos, scale, dmg=0):
        super().__init__(all_sprites)

        self.animation_list = list()
        self.index = 0

        self.dmg = dmg
        self.targets = targets
        self.update_time = pg.time.get_ticks()

        for i in range(6):
            img = pg.image.load("Assets\Animations\effects\Explosion\{0}.png".format(i + 1))
            img = pg.transform.scale(img, (scale[0] * 2, scale[1] * 2))
            self.animation_list.append(img)
        self.image = self.animation_list[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        ANIMATION_COOLDOWN = 100
        if pg.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pg.time.get_ticks()
            self.image = self.animation_list[self.index]
            self.index += 1
        if self.index == len(self.animation_list):
            if self.dmg != 0:
                if pg.sprite.spritecollideany(self, self.targets):
                    hit_targets = [h_t for h_t in self.targets if self.rect.colliderect(h_t.rect)]
                    for hit_target in hit_targets:
                        if pg.sprite.collide_mask(self, hit_target):
                            if hit_target.is_alive():
                                hit_target.change_hp(-self.dmg)
            self.kill()
