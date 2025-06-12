from Scripts.GameObjects.Enemies.Enemy import enemy
import pygame as pg


class melee_enemy(enemy):
    def attack(self):
        if pg.time.get_ticks() - self.atk_cd >= 100 * self.spd_atk:
            self.atk_cd = pg.time.get_ticks()
            self.player.change_hp(-self.atk)
