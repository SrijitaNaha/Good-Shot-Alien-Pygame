import pygame
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
ALIEN_SIZE = 50
ALIEN_SPEED = 5
SCORE_FONT = pygame.font.SysFont('Arial', 24)

class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('alien.png')
        self.image = pygame.transform.scale(self.image, (ALIEN_SIZE, ALIEN_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - ALIEN_SIZE)
        self.rect.y = random.randint(0, HEIGHT - ALIEN_SIZE)

    def move(self):
        self.rect.x = random.randint(0, WIDTH - ALIEN_SIZE)
        self.rect.y = random.randint(0, HEIGHT - ALIEN_SIZE)

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    alien = Alien()
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if alien.rect.collidepoint(event.pos):
                    score += 1
                    alien.move()
                else:
                    score -= 1

        screen.fill((0, 0, 0))
        screen.blit(alien.image, alien.rect)
        score_text = SCORE_FONT.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()