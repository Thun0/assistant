import requests
import pygame
import threading

class Weather:

    #windSpeed = 0
    #windAngle = 0
    #pressure = 0
    #humidity = 0
    #temperature = 0
    #description = ""

    def __init__(self):
        self.get_weather()

    def get_weather(self):
        r = requests.get("http://api.openweathermap.org/data/2.5/weather?id=756135&units=metric&APPID=44b6fc9fc97832f9c8bb1ffcf639b4c4")
        data = r.json()
        self.windSpeed = data["wind"]["speed"]
        self.windAngle = data["wind"]["deg"]
        self.description = data["weather"][0]["description"]
        self.pressure = data["main"]["pressure"]
        self.humidity = data["main"]["humidity"]
        self.temperature = data["main"]["temp"]
        self.conditionId = data["weather"][0]["id"]
        self.time = data["dt"]
        self.sunrise = data["sys"]["sunrise"]
        self.sunset = data["sys"]["sunset"]
        if self.time > self.sunrise and self.time < self.sunset:
            self.night = False
        else:
            self.night = True
        print(data)

    def get_icon(self):
        if self.conditionId > 800 and self.conditionId < 900:
            icon = pygame.image.load("../res/weather/clouds.png")
        else:
            if self.night:
                icon = pygame.image.load("../res/weather/moon.png")
            else:
                icon = pygame.image.load("../res/weather/sun.png")
        return icon
