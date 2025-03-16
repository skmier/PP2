import pygame, os

pygame.init()
pygame.mixer.init()

# screen settings
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Player")

clock = pygame.time.Clock()
font2 = pygame.font.SysFont(None, 20)

# colors
white = (255, 255, 255)

# background
background = pygame.image.load('lab7/images/bgphoto.png')

# button images
play_button = pygame.image.load('lab7/images/play.png')
pause_button = pygame.image.load('lab7/images/pause.png')
next_button = pygame.image.load('lab7/images/next.png')
back_button = pygame.image.load('lab7/images/back.png')

bg = pygame.Surface((500, 200))
bg.fill((255, 255, 255))

# work with music files
music_path = r"C:\Users\saken\OneDrive\Рабочий стол\PP2\lab7\musics"
music_names = [os.path.join(music_path, f) for f in os.listdir(music_path) if f.endswith('.mp3')]

index = 0
play = False  

if music_names:
    pygame.mixer.music.load(music_names[index])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if play:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                play = not play  
            elif event.key == pygame.K_RIGHT and music_names:
                index = (index + 1) % len(music_names)
                pygame.mixer.music.load(music_names[index])
                pygame.mixer.music.play()
                play = True
            elif event.key == pygame.K_LEFT and music_names:
                index = (index - 1) % len(music_names)
                pygame.mixer.music.load(music_names[index])
                pygame.mixer.music.play()
                play = True

    screen.blit(background, (500, 200))
    screen.blit(bg, (350, 500))

    if music_names:
        text2 = font2.render(os.path.basename(music_names[index]), True, (20, 20, 50))
        screen.blit(text2, (500, 520))

    play_button = pygame.transform.scale(play_button, (50, 50))
    pause_button = pygame.transform.scale(pause_button, (50, 50))
    next_button = pygame.transform.scale(next_button, (50, 50))
    back_button = pygame.transform.scale(back_button, (55, 55))
    

    if play:
        screen.blit(pause_button, (550, 600))
    else:
        screen.blit(play_button, (550, 600))

    screen.blit(next_button, (660, 600))
    screen.blit(back_button, (450, 600))

    clock.tick(24)
    pygame.display.update()
