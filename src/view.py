from display import Display
from log import Log
from clock import Clock
from weatherview import WeatherView
import pygame

class View:

    def __init__(self, event_queue):
        Log.i("Creating view")
        self.display = Display()
        self.running = True
        self.clock = Clock()
        self.weatherView = WeatherView()
        self.event_queue = event_queue

    def loop(self):
        while self.running:
            self.handle_input()
            self.redraw()

    def redraw(self):
        self.display.blit()
        self.clock.update()
        self.clock.blit(self.display)
        self.weatherView.blit(self.display)
        pygame.display.flip()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Log.i("Close button clicked")
                self.running = False
                Log.i("Closing display")
            else:
                self.event_queue.put(event)
