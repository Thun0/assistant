import queue
from threading import Thread

import pygame

from controller import Controller
from log import Log
from model import Model
from view import View

from weather import Weather

def main():
    w = Weather()
    Log.init()
    Log.i("Log start")
    pygame.init()
    Log.i("Pygame initialized")
    eventQueue = queue.Queue()
    view = View(eventQueue)
    model = Model()
    controller = Controller(eventQueue, model, view)
    controllerThread = Thread(target=controller.loop)
    controllerThread.daemon = True
    controllerThread.start()
    view.loop()
    pygame.quit()
    Log.i("Quitting")
    Log.dispose()

if __name__ == "__main__":
    main()
