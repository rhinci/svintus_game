import pygame as pg
class PlayerMove:
    #горизонтальное движение
    def move_h(self):
        key = pg.key.get_pressed()
        if key[pg.K_a]:
            return -1
        if key[pg.K_d]:
            return 1
        return 0
    #вертикальное движение
    def move_v(self):
        key = pg.key.get_pressed()
        if key[pg.K_w]:
            return -1
        if key[pg.K_s]:
            return 1
        return 0
    def Border(self,pos,size):
        border = pg.display.get_window_size()
        size = pg.Vector2(size)
        if pos[0] < size[0] / 2:
            pos[0] = size[0] / 2
        if pos[1] < size[1] + 60:
            pos[1] = size[1] + 60
        if pos[0] > border[0] - size[0] / 2:
            pos[0] = border[0] - size[0] / 2
        if pos[1] > border[1] - 75 - size[1] / 2:
            pos[1] = border[1] - 75 - size[1] / 2
        return pos
    def move(self, pos, speed, size):
        pos[0] += speed * self.move_h()
        pos[1] += speed * self.move_v()
        pos = self.Border(pos,size)
        return pos
