from display import Display
from log import Log
from clock import Clock
import pygame


class View:

    def __init__(self, eventQueue):
        Log.i("Creating view")
        self.display = Display()
        self.running = True
        self.clock = Clock()

    def loop(self):
        while self.running:
            self.handleInput()
            self.redraw()

    def redraw(self):
        self.display.blit()
        self.clock.update()
        self.clock.blit(self.display)
        pygame.display.flip()

    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Log.i("Close button clicked")
                self.running = False
                Log.i("Closing display")
