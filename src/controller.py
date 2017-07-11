import event_types


class Controller():

    def __init__(self, event_queue, model, view):
        self.event_queue = event_queue
        self.model = model

    def loop(self):
        while True:
            event = self.event_queue.get(True)
