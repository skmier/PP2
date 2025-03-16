import pygame
import time
import sys

pygame.init()

WIDTH, HEIGHT = 1200, 1200
CENTER = (WIDTH // 2, HEIGHT // 2)  # Центр часов
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")


bg_clock = pygame.transform.scale(pygame.image.load("lab7/images/clock.png"), (WIDTH, HEIGHT))
minute_hand = pygame.image.load('lab7/images/minute.png')
second_hand = pygame.image.load('lab7/images/second.png')

clock = pygame.time.Clock()

while True:
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min

    minute_angle = -(minutes / 60) * 360 + 90
    second_angle = -(seconds / 60) * 360 + 90


    screen.blit(bg_clock, (0, 0))

    
    rotated_minute = pygame.transform.rotate(minute_hand, minute_angle)
    minute_rect = rotated_minute.get_rect()
    minute_rect.center = CENTER  
    screen.blit(rotated_minute, minute_rect.topleft)

    
    rotated_second = pygame.transform.rotate(second_hand, second_angle)
    second_rect = rotated_second.get_rect()
    second_rect.center = CENTER
    screen.blit(rotated_second, second_rect.topleft)

    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)  
