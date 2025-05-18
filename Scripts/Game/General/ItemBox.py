import pygame as pg

class itemBox(pg.sprite.Sprite):
    def __init__(self,all_sprites,config,player,pos):
        super().__init__(all_sprites)
        self.item_type = config['item_type']
        self.image = pg.image.load(config['image'])
        self.rect = self.image.get_rect()
        self.rect.midtop = (pos)
        self.player = player
    def collision(self):
        pass
    def update(self):
        self.collision()

class health_pack(itemBox):
    def collision(self):
        if pg.sprite.collide_rect(self,self.player):
            self.player.change_hp(5)
            self.kill()
class exp_pack(itemBox):
    def collision(self):
        if pg.sprite.collide_rect(self,self.player):
            self.player.change_exp(5)
            self.kill()
