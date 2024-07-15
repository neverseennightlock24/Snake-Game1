import pygame
import random

pygame.init()
pygame.display.set_caption("Snake Game")
screen = pygame.display.set_mode((800, 800))
# This versison allows for Snake overlap at the cost of imprecisse Apple spawning

WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 50, 50]
GREEN = [0, 255, 0]
BLUE = [0, 127, 255]
YELLOW = [255, 255, 0]
PURPLE = [127, 0, 255]

snake_x = 400
snake_y = 400
snake_rect = pygame.Rect(snake_x, snake_y, 20, 20)
snake_segments = [snake_rect]

snake_dx = 0
snake_dy = 0

apple_x = random.randint(40, 760)
apple_y = random.randint(40, 760)
apple_rect = pygame.Rect(apple_x, apple_y, 20, 20)

score = 0
game_over = False

FPS = 30
fpsClock = pygame.time.Clock()

def restart_game():
    global snake_x, snake_y, snake_rect, snake_segments, snake_dx, snake_dy, apple_x, apple_y, apple_rect, score, game_over
    snake_x = 400
    snake_y = 400
    snake_rect = pygame.Rect(snake_x, snake_y, 20, 20)
    snake_segments = [snake_rect]
    snake_dx = 0
    snake_dy = 0
    apple_x = random.randint(40, 760)
    apple_y = random.randint(40, 760)
    apple_rect = pygame.Rect(apple_x, apple_y, 20, 20)
    score = 0
    game_over = False

def main_game_loop():
    global snake_x, snake_y, snake_rect, snake_segments, snake_dx, snake_dy, apple_x, apple_y, apple_rect, score, game_over

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_dx = -20
                    snake_dy = 0
                elif event.key == pygame.K_RIGHT:
                    snake_dx = 20
                    snake_dy = 0
                elif event.key == pygame.K_UP:
                    snake_dx = 0
                    snake_dy = -20
                elif event.key == pygame.K_DOWN:
                    snake_dx = 0
                    snake_dy = 20
            elif event.type == pygame.QUIT:
                pygame.quit()
                exit()

        snake_x += snake_dx
        snake_y += snake_dy

        snake_rect = pygame.Rect(snake_x, snake_y, 20, 20)
        snake_segments.append(snake_rect)

        if snake_x < 30 or snake_x >= 760 or snake_y < 30 or snake_y >= 760:
            game_over = True

        if snake_rect.colliderect(apple_rect):
            score += 1
            apple_x = random.randint(40, 760)
            apple_y = random.randint(40, 760)
            apple_rect = pygame.Rect(apple_x, apple_y, 20, 20)

        if len(snake_segments) > score + 1:
            snake_segments.pop(0)

        screen.fill(BLACK)
        pygame.draw.rect(screen, BLUE, (20, 20, 760, 760))
        
        for segment in snake_segments:
            pygame.draw.rect(screen, GREEN, segment)
        pygame.draw.rect(screen, RED, apple_rect)

        pygame.display.update()

        fpsClock.tick(FPS)

    font = pygame.font.Font('PlayfairDisplay-VariableFont_wght.ttf', 36)
    text = font.render("Game Over! Score: " + str(score), True, GREEN)
    text_rect = text.get_rect(center = (400, 400))
    screen.blit(text, text_rect)
    text2 = font.render("Press SPACE to Continue", True, GREEN)
    text_rect2 = text.get_rect(center = (360, 450))
    screen.blit(text2, text_rect2)

    pygame.display.update()

while True:
    main_game_loop()
    game_over = True
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                restart_game()
                game_over = False
            elif event.type == pygame.QUIT:
                game_over = False
                pygame.quit()
                exit()

        fpsClock.tick(FPS)
