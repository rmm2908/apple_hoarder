import pygame
import random


class Apple:
    def __init__(self, screen, sprite: str):
        self._sprite = pygame.image.load(sprite)
        self._SCREEN = screen
        self.rect = self._sprite.get_rect()

    def reset(self):
        self.rect.x = random.randint(0, self._SCREEN.get_width() - self.rect.width)
        self.rect.y = 0

    def fall(self, speed: int):
        self.rect = self.rect.move((0, speed))

    def draw(self):
        self._SCREEN.blit(self._sprite, self.rect)
