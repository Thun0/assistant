import queue
import pygame
import argparse

from threading import Thread

from controller import Controller
from log import Log
from model import Model
from view import View
from settings import Settings


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fullscreen", help="runs in fullscreen", action="store_true")
    args = parser.parse_args()
    if args.fullscreen:
        Settings.FULLSCREEN = True
    Log.init()
    Log.i("Log start")
    pygame.init()
    Log.i("Pygame initialized")
    event_queue = queue.Queue()
    view = View(event_queue)
    model = Model()
    controller = Controller(event_queue, model, view)
    controller_thread = Thread(target=controller.loop)
    controller_thread.daemon = True
    controller_thread.start()
    view.loop()
    pygame.quit()
    Log.i("Quitting")
    Log.dispose()

if __name__ == "__main__":
    main()
