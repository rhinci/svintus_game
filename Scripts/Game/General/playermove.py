import pygame as pg


class PlayerMove:
    def move_h(self, key):
        if key[pg.K_a]:
            return -1
        if key[pg.K_d]:
            return 1
        return 0

    def move_v(self, key):
        if key[pg.K_w]:
            return -1
        if key[pg.K_s]:
            return 1
        return 0

    def move(self, x, y, speed, event,border,size):
        x += speed * self.move_h(event)
        y += speed * self.move_v(event)
        if x<0:
            x = 0
        if y<0:
            y = 0
        if x>border[0]-size[0]:
            x = border[0]-size[0]
        if y>border[1]-size[1]:
            y = border[1]-size[1]
        return x, y
