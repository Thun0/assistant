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
    Log.init()
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fullscreen", help="runs in fullscreen", action="store_true")
    parser.add_argument("-l", "--log", help="creates log file")
    args = parser.parse_args()
    if args.log:
        Log.init(args.log)
    if args.fullscreen:
        Settings.FULLSCREEN = True
        Log.i("Starting in fullscreen")
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
