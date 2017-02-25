from log import Log
from settings import Settings
import pygame


class Display:

    def __init__(self):
        Log.i("Creating display")
        self.resolution = (Settings.DISPLAY_WIDTH, Settings.DISPLAY_HEIGHT)
        pygame.display.set_caption(Settings.APP_NAME)
        self.screen = pygame.display.set_mode(self.resolution)
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill(Settings.BG_COLOR)
        self.background = self.background.convert()

    def blit(self):
        self.screen.blit(self.background, (0, 0))
