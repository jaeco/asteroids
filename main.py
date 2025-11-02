import pygame as game
from constants import *

def main():
    game.init()
    screen = game.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in game.event.get():
            if event.type == game.QUIT:
                return
        screen.fill("Black")
        game.display.flip()
    
    
    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
