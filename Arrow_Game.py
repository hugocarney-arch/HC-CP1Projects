import sys
import random
import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FNF Style Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
GRAY = (100, 100, 100)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 150, 255)
YELLOW = (255, 255, 50)
PURPLE = (180, 50, 255)

# Fonts
font = pygame.font.SysFont("Arial", 32)
big_font = pygame.font.SysFont("Arial", 64)

# Lane configuration (Left, Down, Up, Right)
KEYS = [pygame.K_LEFT, pygame.K_DOWN, pygame.K_UP, pygame.K_RIGHT]
KEY_NAMES = ["LEFT", "DOWN", "UP", "RIGHT"]
COLORS = [PURPLE, BLUE, GREEN, RED]
X_POSITIONS = [250, 350, 450, 550]
TARGET_Y = 480

# Game variables
score = 0
misses = 0
max_misses = 10
game_over = False
notes = []
spawn_timer = 0
spawn_rate = 45  # frames between note spawns
note_speed = 5

clock = pygame.time.Clock()


def reset_game():
    global score, misses, game_over, notes, spawn_timer
    score = 0
    misses = 0
    game_over = False
    notes = []
    spawn_timer = 0


# Main game loop
while True:
    # STABILITY FIX: Pump internal events to keep the VS Code window active
    pygame.event.pump() 
    
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            # Click anywhere to restart
            reset_game()

        if event.type == pygame.KEYDOWN and not game_over:
            for i in range(4):
                if event.key == KEYS[i]:
                    # Check if a note is close to TARGET_Y in lane i
                    hit = False
                    for note in notes[:]:
                        if note["lane"] == i and abs(note["y"] - TARGET_Y) < 45:
                            score += 100
                            notes.remove(note)
                            hit = True
                            break
                    if not hit:
                        # Bad hit / extra press counts as a miss
                        misses += 1
                        if misses >= max_misses:
                            game_over = True

    if not game_over:
        # Spawn notes
        spawn_timer += 1
        if spawn_timer >= spawn_rate:
            lane = random.randint(0, 3)
            notes.append({"lane": lane, "y": -50})
            spawn_timer = 0

        # Move notes
        for note in notes[:]:
            note["y"] += note_speed
            # Check if note passed the screen
            if note["y"] > HEIGHT:
                notes.remove(note)
                misses += 1
                if misses >= max_misses:
                    game_over = True

    # Draw Targets / Receptors
    for i in range(4):
        pygame.draw.circle(screen, COLORS[i], (X_POSITIONS[i], TARGET_Y), 35, 3)
        label = font.render(KEY_NAMES[i][0], True, COLORS[i])
        screen.blit(label, (X_POSITIONS[i] - 10, TARGET_Y - 18))

    # Draw Falling Notes
    for note in notes:
        x = X_POSITIONS[note["lane"]]
        y = note["y"]
        pygame.draw.circle(screen, COLORS[note["lane"]], (x, int(y)), 25)

    # Draw Score and Misses
    score_text = font.render(f"Score: {score}", True, WHITE)
    miss_text = font.render(f"Misses: {misses}/{max_misses}", True, RED)
    screen.blit(score_text, (30, 30))
    screen.blit(miss_text, (30, 70))

    # Game Over Screen
    if game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))

        go_text = big_font.render("GAME OVER", True, RED)
        restart_text = font.render("Click anywhere to Restart", True, WHITE)

        screen.blit(go_text, (WIDTH // 2 - go_text.get_width() // 2, HEIGHT // 2 - 60))
        screen.blit(
            restart_text,
            (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 20),
        )

    pygame.display.flip()
    clock.tick(60)
