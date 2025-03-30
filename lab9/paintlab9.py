import pygame
import random

pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint in Pygame")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

colors = [BLACK, RED, GREEN, BLUE]
current_color = BLACK

is_drawing = False
mode = "pen"
start_pos = None

screen.fill(WHITE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                is_drawing = True
                start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                is_drawing = False
                end_pos = event.pos

                if mode == "rectangle":
                    pygame.draw.rect(screen, current_color, (*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 2)
                elif mode == "square":
                    side = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    pygame.draw.rect(screen, current_color, (start_pos[0], start_pos[1], side, side), 2)
                elif mode == "circle":
                    radius = int(((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2) ** 0.5)
                    pygame.draw.circle(screen, current_color, start_pos, radius, 2)
                elif mode == "right_triangle":
                    pygame.draw.polygon(screen, current_color, [start_pos, (start_pos[0], end_pos[1]), end_pos], 2)
                elif mode == "equilateral_triangle":
                    height = abs(end_pos[1] - start_pos[1])
                    base_half = height / (3 ** 0.5)
                    pygame.draw.polygon(screen, current_color, [
                        (start_pos[0], start_pos[1] - height), 
                        (start_pos[0] - base_half, start_pos[1]), 
                        (start_pos[0] + base_half, start_pos[1])
                    ], 2)
                elif mode == "rhombus":
                    width = abs(end_pos[0] - start_pos[0])
                    height = abs(end_pos[1] - start_pos[1])
                    pygame.draw.polygon(screen, current_color, [
                        (start_pos[0], start_pos[1] - height // 2), 
                        (start_pos[0] + width // 2, start_pos[1]), 
                        (start_pos[0], start_pos[1] + height // 2), 
                        (start_pos[0] - width // 2, start_pos[1])
                    ], 2)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rectangle"
            elif event.key == pygame.K_s:
                mode = "square"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_p:
                mode = "pen"
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_t:
                mode = "right_triangle"
            elif event.key == pygame.K_q:
                mode = "equilateral_triangle"
            elif event.key == pygame.K_h:
                mode = "rhombus"
            elif event.key == pygame.K_1:
                current_color = BLACK
            elif event.key == pygame.K_2:
                current_color = RED
            elif event.key == pygame.K_3:
                current_color = GREEN
            elif event.key == pygame.K_4:
                current_color = BLUE

    if is_drawing and mode == "pen":
        pygame.draw.circle(screen, current_color, pygame.mouse.get_pos(), 3)
    elif is_drawing and mode == "eraser":
        pygame.draw.circle(screen, WHITE, pygame.mouse.get_pos(), 10)

    pygame.display.update()

pygame.quit()
