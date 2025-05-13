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

    def move(self, pos, speed, size):
        border = pg.display.get_window_size()
        keys = pg.key.get_pressed()
        pos[0] += speed * self.move_h(keys)
        pos[1] += speed * self.move_v(keys)
        if pos[0] < 0:
            pos[0] = 0
        if pos[1] < 0:
            pos[1] = 0
        if pos[0] > border[0] - size[0] / 2:
            pos[0] = border[0] - size[0] / 2
        if pos[1] > border[1] - size[1] / 2:
            pos[1] = border[1] - size[1] / 2
        return pos
