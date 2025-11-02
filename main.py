import pygame as game
from player import Player
from constants import *

def main():
    game.init()
    screen = game.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = game.time.Clock()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0
    while True:
        for event in game.event.get():
            if event.type == game.QUIT:
                return
        screen.fill("Black")
        dt = clock.tick(60) / 1000
        player.update(dt)
        player.draw(screen)
        game.display.flip()
if __name__ == "__main__":
    main()
