import pygame as pg


class PlayerMove:
    def move_h(self):
        key = pg.key.get_pressed()
        if key[pg.K_a]:
            return -1
        if key[pg.K_d]:
            return 1
        return 0

    def move_v(self):
        key = pg.key.get_pressed()
        if key[pg.K_w]:
            return -1
        if key[pg.K_s]:
            return 1
        return 0

    def move(self, pos, speed, size):
        border = pg.display.get_window_size()
        size = pg.Vector2(size)
        pos[0] += speed * self.move_h()
        pos[1] += speed * self.move_v()
        if pos[0] < size[0] / 2:
            pos[0] = size[0] / 2
        if pos[1] < size[1]:
            pos[1] = size[1]
        if pos[0] > border[0] - size[0] / 2:
            pos[0] = border[0] - size[0] / 2
        if pos[1] > border[1] - 75 - size[1] / 2:
            pos[1] = border[1] - 75 - size[1] / 2
        return pos
