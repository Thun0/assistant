import pygame


class Button:

    def __init__(self, path):
        self.x = 0
        self.y = 0
        self.img = pygame.image.load(path)
        self.w = self.img.get_width()
        self.h = self.img.get_height()

    def set_xy(self, x, y):
        self.x = x
        self.y = y

    def set_dimensions(self, w, h):
        self.w = w
        self.h = h
        self._resize()

    def set_width(self, w):
        self.w = w
        self._resize()

    def set_height(self, h):
        self.h = h
        self._resize()

    def _resize(self):
        self.img = pygame.transform.scale(self.img, (self.w, self.h))