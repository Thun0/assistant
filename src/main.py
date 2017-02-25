from view import View
from log import Log
from model import Model
from controller import Controller
import pygame
import queue
from threading import Thread

def main():
    Log.init()
    Log.i("Log start")
    pygame.init()
    Log.i("Pygame initialized")
    eventQueue = queue.Queue()
    view = View(eventQueue)
    model = Model()
    controller = Controller(eventQueue, model, view)
    controllerThread = Thread(target = controller.loop)
    controllerThread.daemon = True
    controllerThread.start()
    view.loop()
    pygame.quit()
    Log.i("Quitting")
    Log.dispose()

if __name__ == "__main__":
    main()
