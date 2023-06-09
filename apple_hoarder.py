import pygame
import random


class Game:
    def __init__(self, fps: int, screen_xy: tuple, lives: int, speed: int, apple: str, bg: str, *sprites: str):
        self._score = 0
        self._FPS = fps
        self._left_pressed = False
        self._right_pressed = False
        self._running = True
        self._BACKGROUND = pygame.image.load(bg)
        self._CLOCK = pygame.time.Clock()
        self._lives = lives
        self._speed = speed
        self.SCREEN = pygame.display.set_mode(screen_xy)
        self._BASKET = Basket(self.SCREEN, sprites)
        self._APPLE = Apple(self.SCREEN, apple)
        self._font = pygame.font.Font('sprites/Pixels.ttf', 50)

    def display_stats(self):
        score = self._font.render(f'SCORE: {self._score}', False, pygame.color.Color(0, 0, 0))
        speed = self._font.render(f'SPEED: {self._speed}', False, pygame.color.Color(0, 0, 0))
        lives = self._font.render(f'LIVES: {self._lives}', False, pygame.color.Color(0, 0, 0))

        self.SCREEN.blit(score, (10, 10))
        self.SCREEN.blit(speed, (self.SCREEN.get_width()//2-speed.get_width()//2, 10))
        self.SCREEN.blit(lives, (self.SCREEN.get_width()-lives.get_width(), 10))

    def render_bg(self):
        self.SCREEN.blit(self._BACKGROUND, (0, 0))

    def run(self):
        frame_counter = 0
        frame = 0
        speed_counter = 0
        jp = False
        self._APPLE.reset()

        while self._running:
            self._CLOCK.tick(self._FPS)

            if speed_counter > 0 and speed_counter % 10 == 0:
                self._speed += 2
                speed_counter = 0

            frame_counter += 1
            if frame_counter == 1:
                frame = 0
            elif frame_counter == 5:
                frame = 1
            elif frame_counter == 10:
                frame = 2
            elif frame_counter == 15:
                frame_counter = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self._left_pressed = True
                        jp = True
                    elif event.key == pygame.K_RIGHT:
                        self._right_pressed = True
                        jp = False
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self._left_pressed = False
                    elif event.key == pygame.K_RIGHT:
                        self._right_pressed = False

            self.render_bg()
            self.display_stats()

            if self._left_pressed:
                self._BASKET.move('l')
                self._BASKET.draw(frame, True)
            elif self._right_pressed:
                self._BASKET.move('r')
                self._BASKET.draw(frame, False)
            else:
                self._BASKET.draw(0, jp)

            self._APPLE.fall(self._speed)
            self._APPLE.draw()

            if self._BASKET.rect.colliderect(self._APPLE.rect):
                self._score += 1
                speed_counter += 1
                self._APPLE.reset()
                print('You caught the apple')
            if self._APPLE.rect.y + self._APPLE.rect.height >= self.SCREEN.get_height():
                self._lives -= 1
                self._APPLE.reset()
                print('You missed the apple!')

            if self._lives < 0:
                self._running = False

            pygame.display.update()

        print("""
        ░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░██╗
        ██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗██║
        ██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝██║
        ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗╚═╝
        ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║██╗
        ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝""")
        print(f'Final Score: {self._score}')
        pygame.quit()


class Basket:
    def __init__(self, screen, sprites: tuple[str]):
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


class Apple:
    def __init__(self, screen, sprite: str):
        self._sprite = pygame.image.load(sprite)
        self._SCREEN = screen
        self.rect = self._sprite.get_rect()
        
    def reset(self):
        self.rect.x = random.randint(0, self._SCREEN.get_width()-self.rect.width)
        self.rect.y = 0
    
    def fall(self, speed: int):
        self.rect = self.rect.move((0, speed))

    def draw(self):
        self._SCREEN.blit(self._sprite, self.rect)


def main():
    fps = 60
    screen_res = (800, 600)
    lives = 3
    speed = 3
    pygame.init()
    game = Game(fps, screen_res, lives, speed,
                'sprites/apple.png', 'sprites/bg.png', 'sprites/basket_f0.png', 'sprites/basket_f1.png', 'sprites/basket_f2.png')
    pygame.display.set_caption('Apple Hoarder')
    game.run()


if __name__ == '__main__':
    main()
