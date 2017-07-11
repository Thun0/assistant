from settings import Settings
import pygame
from view_component import ViewComponent
from log import Log


class WeatherView(ViewComponent):

    def __init__(self, weather):
        self.x = Settings.WEATHER_X
        self.y = Settings.WEATHER_Y
        self.weather = weather
        self._conditions_icon = self.weather.get_icon()

        self._temperature_font = pygame.font.SysFont(Settings.TEMPERATURE_FONT, int(Settings.TEMPERATURE_FONT_SIZE))
        self._weather_description_font = pygame.font.SysFont(
            Settings.WEATHER_DESCRIPTION_FONT, int(Settings.WEATHER_DESCRIPTION_FONT_SIZE))
        self._outside_temp_view = self._temperature_font.render(
            "Outside: " + str(self.weather.temperature) + " \u00b0C", True, (255, 255, 255))

    def update(self):
        Log.i("Updating weather view")
        self.weather.get_weather()
        self._conditions_icon = self.weather.get_icon()
        self._outside_temp_view = self._temperature_font.render(
            "Outside: " + str(self.weather.temperature) + " \u00b0C", True, (255, 255, 255))

    def blit(self, display):
        display.screen.blit(self._conditions_icon, (self.x, self.y))
        display.screen.blit(self._outside_temp_view, (self.x, self.y + 300))
