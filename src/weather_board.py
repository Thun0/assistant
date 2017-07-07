import io


class WeatherBoard:

    def __init__(self):
        self.dev_path = "/dev/i2c-1"
        f = io.open(self.dev_path, 'r+')
        text = f.read()
        print(text)

    def si1132_init(self):
        pass
