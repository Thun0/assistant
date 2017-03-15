from weather import Weather
from settings import Settings
import pygame

class WeatherView:

    def __init__(self):
        self.x = Settings.WEATHER_X
        self.y = Settings.WEATHER_Y
        self.weather = Weather()
        self.icon = self.weather.getIcon()

        self.temperatureFont = pygame.font.SysFont(Settings.TEMPERATURE_FONT, int(Settings.TEMPERATURE_FONT_SIZE))
        self.weatherDescriptionFont = pygame.font.SysFont(Settings.WEATHER_DESCRIPTION_FONT, int(Settings.WEATHER_DESCRIPTION_FONT_SIZE))

    def update(self):
        self.weather.getWeather()
        self.icon = self.weather.getIcon()

    def blit(self, display):
        display.screen.blit(self.icon, (self.x, self.y))
