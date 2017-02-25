from display import Display
from log import Log

class View:
    def __init__(self, eventQueue):
        Log.i("Creating view")
        display = Display()
