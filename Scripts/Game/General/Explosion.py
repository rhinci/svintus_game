import pygame as pg

class explosion(pg.sprite.Sprite):
    def __init__(self,all_sprites,pos,scale):
        super().__init__(all_sprites)
        self.animation_list = list()
        self.index = 0
        self.update_time = pg.time.get_ticks()
        for i in range (6):
            img = pg.image.load("Scripts\Game\General\Assets\Animations\Explosion\{0}.png".format(i+1))
            img = pg.transform.scale(img,(scale[0]*2,scale[1]*2))
            self.animation_list.append(img)
        self.image = self.animation_list[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = pos
    def update(self):
        ANIMATION_COOLDOWN = 100
        if pg.time.get_ticks()-self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pg.time.get_ticks()
            self.image = self.animation_list[self.index]
            self.index +=1
        if self.index == len(self.animation_list):
            self.kill()
