import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"
change_to = snake_direction
speed = 15

def generate_food():
    while True:
        pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
        if pos not in snake_body:
            return pos

food_pos = generate_food()
food_spawn = True

game_score = 0
level = 1
level_threshold = 3

isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                change_to = "UP"
            if event.key == pygame.K_DOWN and snake_direction != "UP":
                change_to = "DOWN"
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                change_to = "RIGHT"

    snake_direction = change_to
    if snake_direction == "UP":
        snake_pos[1] -= 10
    elif snake_direction == "DOWN":
        snake_pos[1] += 10
    elif snake_direction == "LEFT":
        snake_pos[0] -= 10
    elif snake_direction == "RIGHT":
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))

    if snake_pos == food_pos:
        food_spawn = False
        game_score += 1
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = generate_food()
    food_spawn = True

    if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
        isRunning = False

    for block in snake_body[1:]:
        if snake_pos == block:
            isRunning = False

    if game_score % level_threshold == 0 and game_score != 0:
        level = game_score // level_threshold + 1
        speed = 15 + (level - 1) * 3

    screen.fill(BLACK)
    for p in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(p[0], p[1], 10, 10))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    score_text = font.render(f"Score: {game_score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (20, 20))
    screen.blit(level_text, (20, 50))

    pygame.display.update()
    clock.tick(speed)

game_over_text = font.render("GAME OVER", True, WHITE)
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (WIDTH / 2, HEIGHT / 2)
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(3000)

pygame.quit()
