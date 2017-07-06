import event_types

class Controller():

    def __init__(self, event_queue, model, view):
        self.event_queue = event_queue
        self.model = model

    def loop(self):
        while True:
            event = self.event_queue.get(True)
            if event.type == event_types.WEATHER_UPDATE_EVENT:
                self.model.update_weather()
