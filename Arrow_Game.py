import random
import sys
import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FNF - Ultra Hard Bot Mode")

# Colors
BLACK = (15, 15, 15)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
COLORS = [(255, 0, 85), (0, 255, 119), (0, 170, 255), (255, 170, 0)]  # Left, Down, Up, Right
GLOW_COLORS = (255, 255, 255)

# Lane positions (X coordinates)
LANES = [250, 350, 450, 550]
KEY_NAMES = ["LEFT", "DOWN", "UP", "RIGHT"]

# Game variables
CLOCK = pygame.time.Clock()
FPS = 60
NOTE_SPEED = 10  # Extremely fast/hard
SPAWN_CHANCE = 0.18  # High frequency of notes

notes = []  # List to store active notes: [lane, y_position]
score = 0
combo = 0
max_combo = 0
hit_effects = [0, 0, 0, 0]  # Visual flash timers for receptors

# Generate initial notes
def spawn_note():
  lane = random.randint(0, 3)
  notes.append([lane, -50])


# Main Game Loop
running = True
while running:
  screen.fill(BLACK)

  # Event handling
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = false

  # Spawn notes rapidly (Ultra Hard)
  if random.random() < SPAWN_CHANCE:
    spawn_note()

  # Update notes positions
  for note in notes[:]:
    note[1] += NOTE_SPEED

    # Receptors (target area) are at Y = 100
    # The bot automatically "hits" the note when it reaches Y = 100
    if 90 <= note[1] <= 110:
      hit_effects[note[0]] = 10  # Trigger visual press
      score += 350
      combo += 1
      if combo > max_combo:
        max_combo = combo
      notes.remove(note)
    elif note[1] > HEIGHT:
      # Miss if it somehow passes
      notes.remove(note)
      combo = 0

  # Draw static receptors at Y = 100
  for i in range(4):
    color = COLORS[i] if hit_effects[i] > 0 else GRAY
    if hit_effects[i] > 0:
      hit_effects[i] -= 1
    pygame.draw.circle(screen, color, (LANES[i], 100), 40, 4)

  # Draw falling notes
  for note in notes:
    lane = note[0]
    y = note[1]
    pygame.draw.circle(screen, COLORS[lane], (LANES[lane], int(y)), 35)

  # Draw UI / HUD
  font = pygame.font.SysFont("Arial", 28)
  score_text = font.render(f"SCORE: {score}", True, WHITE)
  combo_text = font.render(f"COMBO: {combo} (MAX: {max_combo})", True, WHITE)
  bot_text = font.render("BOTPLAY ACTIVE", True, (255, 50, 50))

  screen.blit(score_text, (20, 20))
  screen.blit(combo_text, (20, 60))
  screen.blit(bot_text, (WIDTH - 220, 20))

  pygame.display.flip()
  CLOCK.tick(FPS)

pygame.quit()
sys.exit()
