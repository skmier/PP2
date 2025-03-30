import pygame, sys, random, time
from pygame.locals import *

pygame.init()
pygame.mixer.init()

# FPS
clock = pygame.time.Clock()

# Colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH, HEIGHT = 400, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RACER V2.2")

speed = 5
coins_collected = 0
score = 0
N = 5   

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Background
background_img = pygame.image.load("lab8/racer/AnimatedStreet.png")
screen.fill(WHITE)

# Music
pygame.mixer.music.load("lab8/racer/background.wav")
pygame.mixer.music.play(-1)

# Coin
coin_image = pygame.image.load("lab8/racer/Coin.png")
coin_image = pygame.transform.scale(coin_image, (30, 30))

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/racer/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.top > HEIGHT:
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)

# Player class
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
        if pressed_keys[K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(5, 0)

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), random.randint(-100, -30))

    def move(self):
        self.rect.move_ip(0, speed // 2)
        if self.rect.top > HEIGHT:
            self.respawn()

    def respawn(self):
        self.rect.center = (random.randint(40, WIDTH - 40), random.randint(-100, -30))

P1 = Player()
E1 = Enemy()
coins = pygame.sprite.Group()
for _ in range(3):  # Начальное количество монет
    coin = Coin()
    coins.add(coin)

enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(*coins)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background_img, (0, 0))

    # Display score
    score_display = font_small.render(f"Score: {score}", True, BLACK)
    screen.blit(score_display, (10, 10))

    # Display collected coins
    coin_display = font_small.render(f"Coins: {coins_collected}", True, BLACK)
    screen.blit(coin_display, (WIDTH - 100, 10))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    P1.move()

    # Check for collisions with enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        crash_sound = pygame.mixer.Sound("lab8/racer/crash.wav")
        crash_sound.play()
        pygame.time.delay(1000)

        screen.fill(RED)
        screen.blit(game_over, (30, 250))
        pygame.display.update()

        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Check for coin collection
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)
    for _ in collected_coins:
        coins_collected += 1
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    # Increase enemy speed after collecting N coins
    if coins_collected >= N:
        speed += 1  
        coins_collected = 0  

    pygame.display.update()
    clock.tick(30)
