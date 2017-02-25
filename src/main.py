from view import View
from log import Log
from model import Model
from controller import Controller
import pygame
import queue

def main():
    Log.init()
    Log.i("Log start")
    pygame.init()
    Log.i("Pygame initialized")
    eventQueue = queue.Queue()
    view = View(eventQueue)
    model = Model()
    controller = Controller(eventQueue, model, view)
    controller.start()
    Log.dispose()

if __name__ == "__main__":
    main()
