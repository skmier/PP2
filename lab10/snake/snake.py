import psycopg2, pygame, random, sys
from configsnake import port, db_name, host, user, password


pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

WHITE, GREEN, RED, BLACK = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 0)


def connect_db():
    return psycopg2.connect(
        dbname=db_name, user=user, password=password, host=host, port=port
    )

def get_or_create_user(username):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT id, score, level FROM users WHERE name=%s", (username,))
    user = cur.fetchone()
    if user:
        user_id, score, level = user
    else:
        cur.execute("INSERT INTO users (name) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        score, level = 0, 1
        conn.commit()
    conn.close()
    return user_id, score, level

def update_user_score(user_id, score, level):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE users SET score = %s, level = %s WHERE id = %s", (score, level, user_id))
    conn.commit()
    conn.close()

def generate_food(snake_body):
    while True:
        pos = [random.randrange(1, WIDTH // 10) * 10, random.randrange(1, HEIGHT // 10) * 10]
        if pos not in snake_body:
            return pos


username = input("Введите имя игрока: ")
user_id, game_score, level = get_or_create_user(username)
speed = 15 + (level - 1) * 3
level_threshold = 3

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"
change_to = snake_direction
food_pos = generate_food(snake_body)
food_spawn = True
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                change_to = "RIGHT"
            elif event.key == pygame.K_s:
                update_user_score(user_id, game_score, level)
            elif event.key == pygame.K_p:
                paused = True
                pause_text = font.render("PAUSE — Нажми P для продолжения", True, WHITE)
                screen.blit(pause_text, (WIDTH // 2 - 120, HEIGHT // 2))
                pygame.display.update()
                while paused:
                    for ev in pygame.event.get():
                        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_p:
                            paused = False

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
        food_pos = generate_food(snake_body)
    food_spawn = True

    if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
        break
    if snake_pos in snake_body[1:]:
        break

    if game_score % level_threshold == 0 and game_score != 0:
        level = game_score // level_threshold + 1
        speed = 15 + (level - 1) * 3

    screen.fill(BLACK)
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], 10, 10))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    screen.blit(font.render(f"Score: {game_score}", True, WHITE), (10, 10))
    screen.blit(font.render(f"Level: {level}", True, WHITE), (10, 40))
    pygame.display.update()
    clock.tick(speed)


update_user_score(user_id, game_score, level)
screen.fill(BLACK)
end_text = font.render("GAME OVER", True, WHITE)
screen.blit(end_text, end_text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
pygame.display.update()
pygame.time.wait(3000)
pygame.quit()
