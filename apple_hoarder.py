import pygame
from apple_hoarder import Game


def main():
    fps = 60
    screen_res = (800, 600)
    lives = 3
    speed = 3
    pygame.init()
    game = Game(fps, screen_res, lives, speed,
                'sprites/apple.png', 'sprites/bg.png', 'sprites/basket_f0.png', 'sprites/basket_f1.png',
                'sprites/basket_f2.png')
    pygame.display.set_caption('Apple Hoarder')
    game.run()


if __name__ == '__main__':
    main()
