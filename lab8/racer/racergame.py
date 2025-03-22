import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

SPEED = 5
SCORE = 0
COINS_COLLECTED = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("lab8/racer/AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

pygame.mixer.init()
pygame.mixer.music.load("lab8/racer/background.wav")
pygame.mixer.music.play(-1)

coin_image = pygame.image.load("lab8/racer/Coin.png")
coin_image = pygame.transform.scale(coin_image, (30, 30))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/racer/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/racer/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(-100, -30))

    def move(self):
        self.rect.move_ip(0, SPEED // 2)
        if self.rect.top > SCREEN_HEIGHT:
            self.respawn()

    def respawn(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(-100, -30))

P1 = Player()
E1 = Enemy()

coins = pygame.sprite.Group()
for _ in range(3):
    coin = Coin()
    coins.add(coin)

enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(*coins)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))

    score_display = font_small.render(f"Score: {SCORE}", True, BLACK)
    DISPLAYSURF.blit(score_display, (10, 10))

    coin_display = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    DISPLAYSURF.blit(coin_display, (SCREEN_WIDTH - 100, 10))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    P1.move()

    if pygame.sprite.spritecollideany(P1, enemies):
        crash_sound = pygame.mixer.Sound("lab8/racer/crash.wav")
        crash_sound.play()
        pygame.time.delay(1000)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()

        time.sleep(2)
        pygame.quit()
        sys.exit()

    collected_coins = pygame.sprite.spritecollide(P1, coins, True)
    for _ in collected_coins:
        COINS_COLLECTED += 1
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)  

    pygame.display.update()
    FramePerSec.tick(FPS)
