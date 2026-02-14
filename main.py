```python
import pygame
import sys
import time
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 800
HEIGHT = 600
BLOCK_SIZE = 20

# Set up some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the display
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
FONT = pygame.font.Font(None, 36)

class SnakeGame:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.direction = 'RIGHT'
        self.apple = (400, 300)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Game logic here

            # Draw everything
            SCREEN.fill(BLACK)
            for x, y in self.snake:
                pygame.draw.rect(SCREEN, WHITE, (x, y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(SCREEN, (255, 0, 0), (self.apple[0], self.apple[1], BLOCK_SIZE, BLOCK_SIZE))

            # Update the display
            pygame.display.flip()
            self.clock.tick(10)

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
```