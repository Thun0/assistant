from settings import Settings
import pygame
import datetime
import calendar

class Clock:

    def __init__(self):
        self.clockFont = pygame.font.SysFont(Settings.CLOCK_FONT, int(Settings.CLOCK_FONT_SIZE))
        self.dateFont = pygame.font.SysFont(Settings.DATE_FONT, int(Settings.DATE_FONT_SIZE))
        self.clockX = Settings.CLOCK_X
        self.clockY = Settings.CLOCK_Y
        self.color = Settings.CLOCK_COLOR
        self.clockText = ""
        self.clockSurface = None
        self.hours = self.minutes = self.seconds = 0
        self.day = self.month = self.year = ""
        self.dateText = self.dayOfWeekText = ""
        self.dateSurface = self.dayOfWeekSurface = None
        self.separator = "/"

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
        self.clockSurface = self.clockFont.render(self.clockText, True, self.color)

        self.day = now.day
        self.month = now.month
        self.year = now.year
        self.dateText = str(self.day) + self.separator + str(self.month) + self.separator + str(self.year)
        self.dayOfWeekText = calendar.day_name[datetime.datetime.today().weekday()]
        self.dateSurface = self.dateFont.render(self.dateText, True, self.color)
        self.dayOfWeekSurface = self.dateFont.render(self.dayOfWeekText, True, self.color)


    def blit(self, display):
        display.screen.blit(self.clockSurface, (self.clockX, self.clockY))
        display.screen.blit(self.dateSurface, (Settings.DATE_X, Settings.DATE_Y))
        display.screen.blit(self.dayOfWeekSurface, (Settings.DATE_X, Settings.DATE_Y + 30))