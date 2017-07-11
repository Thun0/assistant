import pygame
from gi.overrides import override

from view_component import ViewComponent


class Button(ViewComponent):

    def __init__(self, path):
        self.x = 0
        self.y = 0
        self.img = pygame.image.load(path)
        self.w = self.img.get_width()
        self.h = self.img.get_height()

    @override
    def set_dimensions(self, w, h):
        self.w = w
        self.h = h
        self._resize()

    @override
    def set_width(self, w):
        self.w = w
        self._resize()

    @override
    def set_height(self, h):
        self.h = h
        self._resize()

    def _resize(self):
        self.img = pygame.transform.scale(self.img, (self.w, self.h))

    def blit(self, display):
        display.screen.blit(self.img, (self.x, self.y))
