import pygame


class Basket:
    def __init__(self, screen, sprites: tuple[str, ...]):
        self._SCREEN = screen
        self._sprites = sprites
        self.rect = pygame.image.load(sprites[0]).get_rect()
        self.rect.x = self._SCREEN.get_width()//2-self.rect.width//2
        self.rect.y = (self._SCREEN.get_height()//7)*6
        self._speed = 10

    def move(self, direction):
        if direction == 'l':
            self.rect = self.rect.move((-self._speed, 0))
            if self.rect.x <= 0:
                self.rect.x = 1
        if direction == 'r':
            self.rect = self.rect.move((self._speed, 0))
            if self.rect.x + self.rect.width >= self._SCREEN.get_width():
                self.rect.x = self._SCREEN.get_width()-self.rect.width

    def draw(self, frame: int, flip: bool):
        sprite = pygame.image.load(self._sprites[frame])
        if flip:
            sprite = pygame.transform.flip(sprite, True, False)
        self._SCREEN.blit(sprite, self.rect)
