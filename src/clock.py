from settings import Settings
import pygame
import datetime


class Clock:

    def __init__(self):
        self.font = pygame.font.SysFont(Settings.CLOCK_FONT, int(Settings.CLOCK_FONT_SIZE))
        self.x = Settings.CLOCK_X
        self.y = Settings.CLOCK_Y
        self.color = Settings.CLOCK_COLOR
        self.clockText = ""
        self.clockValue = None
        self.hours = self.minutes = self.seconds = 0

    def update(self):
        now = datetime.datetime.now()
        self.hours = now.hour
        if self.hours < 10:
            self.hours = "0" + str(self.hours)
        self.minutes = now.minute
        if self.minutes < 10:
            self.minutes = "0" + str(self.minutes)
        self.seconds = now.second
        if self.seconds < 10:
            self.seconds = "0" + str(self.seconds)
        self.clockText = str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)
        self.clockValue = self.font.render(self.clockText, True, self.color)

    def blit(self, display):
        display.screen.blit(self.clockValue, (self.x, self.y))