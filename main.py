import pygame as game
from constants import *

def main():
    game.init()
    screen = game.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = game.time.Clock()
    dt = 0
    while True:
        for event in game.event.get():
            if event.type == game.QUIT:
                return
        screen.fill("Black")
        game.display.flip()
        clock.tick(60)
        dt = clock.tick() / 1000
if __name__ == "__main__":
    main()
