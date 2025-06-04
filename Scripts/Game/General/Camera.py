import random
import pygame as pg

class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.smoothness = 0.1  # Коэффициент плавности (0-1)
        self.shake_intensity = 0
        self.shake_duration = 0
        self.shake_timer = 0

    def apply(self, entity):
        """Смещает объект относительно камеры с учетом тряски"""
        offset_x = -self.camera.x
        offset_y = -self.camera.y

        # Добавляем эффект тряски
        if self.shake_timer < self.shake_duration:
            offset_x += random.uniform(-self.shake_intensity, self.shake_intensity)
            offset_y += random.uniform(-self.shake_intensity, self.shake_intensity)
            self.shake_timer += 1/60  # 60 FPS

        return entity.rect.move(offset_x, offset_y)

    def update(self, target):
        """Обновляет положение камеры с плавным следованием"""
        # Целевая позиция камеры (центрирование на игроке)
        x = -target.rect.centerx + self.width // 2
        y = -target.rect.centery + self.height // 2

        # Плавное движение (линейная интерполяция)
        self.camera.x += (x - self.camera.x) * self.smoothness
        self.camera.y += (y - self.camera.y) * self.smoothness

    def shake(self, intensity=5, duration=0.5):
        """Запускает эффект тряски камеры"""
        self.shake_intensity = intensity
        self.shake_duration = duration
        self.shake_timer = 0
