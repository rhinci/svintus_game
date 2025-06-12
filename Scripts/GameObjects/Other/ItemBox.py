import pygame as pg
from Scripts.GameObjects.PlayerScripts.statistics_collector import run_stats


class itemBox(pg.sprite.Sprite):
    def __init__(self, all_sprites, config, player, pos):
        #инициализация отображения
        super().__init__(all_sprites)
        self.item_type = config['item_type']
        self.image = pg.transform.scale(pg.image.load(config['image']),config['size'])
        self.rect = self.image.get_rect()
        self.sound = pg.mixer.Sound(config['sound'])
        self.sound.set_volume(0.5)
        self.channel = pg.mixer.Channel(6)
        self.rect.midtop = pos
        self.player = player

    def collision(self):
        pass

    def update(self):
        self.collision()


class health_pack(itemBox):
    def collision(self):
        #взаимодействие с игроком
        if pg.sprite.collide_rect(self, self.player):
            self.sound.play()
            self.player.change_hp(5)
            self.kill()


class exp_pack(itemBox):
    def collision(self):
        #взаимодействие с игроком
        if pg.sprite.collide_rect(self, self.player):
            if not(self.channel.get_busy()):
                self.sound.play()
            self.player.change_exp(1)
            run_stats.increment_stat("3. Crystals collected")
            self.kill()
