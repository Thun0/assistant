import queue
from threading import Thread

import pygame
from audio_player import AudioPlayer
from controller import Controller
from log import Log
from model import Model
from view import View

from weather import Weather
from weather_board import WeatherBoard


def main():
    # wb = WeatherBoard()
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
    #audio_player = AudioPlayer()
    #audio_player.test()
    view.loop()
    pygame.quit()
    Log.i("Quitting")
    Log.dispose()

if __name__ == "__main__":
    main()
