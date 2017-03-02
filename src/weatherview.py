from weather import Weather

class WeatherView:

    def __init__(self):
        self.weather = Weather()
        self.x = 400
        self.y = 400

    def update(self):
        self.weather.getWeather()

    def blit(self, display):
        pass
