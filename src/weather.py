import requests

class Weather:

    windSpeed = 0
    windAngle = 0
    pressure = 0
    humidity = 0
    temperature = 0
    description = ""

    def __init__(self):
        self.getWeather()

    def getWeather(self):
        r = requests.get("http://api.openweathermap.org/data/2.5/weather?id=756135&APPID=44b6fc9fc97832f9c8bb1ffcf639b4c4")
        data = r.json()
        self.windSpeed = data["wind"]["speed"]
        self.windAngle = data["wind"]["deg"]
        self.description = data["weather"][0]["description"]
        self.pressure = data["main"]["pressure"]
        self.humidity = data["main"]["humidity"]
        self.temperature = data["main"]["temp"]
