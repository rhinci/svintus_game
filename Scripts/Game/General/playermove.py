import pygame as pg


class PlayerMove:
    def move_h(self, event):
        if event.type == pg.K_a:
            return -1
        if event.type == pg.K_d:
            return 1
        return 0

    def move_v(self, event):
        if event.type == pg.K_w:
            return 1
        if event.type == pg.K_s:
            return -1
        return 0

    def move(self, x, y, speed, event):
        if event.type == pg.KEYDOWN:
            x += speed * self.move_h(event)
            y += speed * self.move_v(event)
        return x, y
