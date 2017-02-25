from display import Display
from log import Log
import pygame
import sys

class View:


    def __init__(self, eventQueue):
        Log.i("Creating view")
        display = Display()
        self.running = True;

    def loop(self):
        while(self.running):
            self.handleInput()

    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Log.i("Close button clicked")
                self.running = False
                Log.i("Closing display")