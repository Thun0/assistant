from view import View
from log import Log
import pygame

def main():
    Log.init()
    Log.i("Log start")
    pygame.init()
    Log.i("Pygame initialized")
    view = View()
    Log.dispose()

if __name__ == "__main__":
    main()
