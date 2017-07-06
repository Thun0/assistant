from weather import Weather

class Model:

    def __init__(self):
        self.weather = Weather()

    def update_weather(self):
        self.weather.get_weather()