from weather import Weather
from settings import Settings
import pygame

class WeatherView:

    def __init__(self):
        self.x = Settings.WEATHER_X
        self.y = Settings.WEATHER_Y
        self.weather = Weather()
        self._conditions_icon = self.weather.get_icon()

        self._temperature_font = pygame.font.SysFont(Settings.TEMPERATURE_FONT, int(Settings.TEMPERATURE_FONT_SIZE))
        self._weather_description_font = pygame.font.SysFont(Settings.WEATHER_DESCRIPTION_FONT, int(Settings.WEATHER_DESCRIPTION_FONT_SIZE))

        self._outside_temperature_view = self._temperature_font.render("Outside: " + str(self.weather.temperature) + " \u00b0C", True, (255, 255, 255))

    def update(self):
        self.weather.get_weather()
        self._conditions_icon = self.weather.get_icon()

    def blit(self, display):
        display.screen.blit(self._conditions_icon, (self.x, self.y))
        display.screen.blit(self._outside_temperature_view, (self.x, self.y + 300))
