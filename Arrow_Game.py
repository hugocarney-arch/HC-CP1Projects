import pygame
import random
import sys

# 1. Initialize Pygame
pygame.init()

# 2. Game Window Configurations
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python FNF - Arrow Rhythm Game (Game Over & Restart)")
clock = pygame.time.Clock()
FPS = 60

# 3. Colors (RGB)
BLACK  = (10, 10, 15)
WHITE  = (255, 255, 255)
GRAY   = (50, 50, 60)
RED    = (255, 50, 50)     # Left
DOWN_B = (0, 200, 255)     # Down (Light Blue)
UP_G   = (50, 255, 50)     # Up (Green)
PINK   = (255, 50, 255)    # Right

# 4. Lanes Mapping (Index: 0=Left, 1=Down, 2=Up, 3=Right)
LANES = [0, 1, 2, 3]
LANE_X = [250, 320, 390, 460]  # Screen X positions for lanes
LANE_COLORS = [RED, DOWN_B, UP_G, PINK]
KEY_MAP = {
    pygame.K_LEFT: 0,
    pygame.K_DOWN: 1,
    pygame.K_UP: 2,
    pygame.K_RIGHT: 3
}

# 5. Core Game Variables
STRUM_Y = 100         # Y position of the target receptors
BASE_SPEED = 6        # Starting speed of arrows
arrow_speed = BASE_SPEED
SPAWN_RATE = 45       # Frames between new arrow spawns
spawn_timer = 0
score = 0
streak = 0
miss_count = 0
MAX_MISSES = 10
game_over = False

rating_text = ""
rating_color = WHITE
rating_timer = 0

# Fonts
font_score = pygame.font.SysFont("Arial", 24, bold=True)
font_rating = pygame.font.SysFont("Arial", 40, bold=True)
font_game_over = pygame.font.SysFont("Arial", 64, bold=True)
font_restart = pygame.font.SysFont("Arial", 28, bold=True)

# 6. Game Classes
class Arrow:
    def __init__(self, lane):
        self.lane = lane
        self.x = LANE_X[lane]
        self.y = SCREEN_HEIGHT + 20  # Spawn off-screen at the bottom
        self.color = LANE_COLORS[lane]
        self.size = 50
        self.active = True

    def update(self):
        global arrow_speed
        self.y -= arrow_speed  # Move upward using the dynamic speed
        if self.y < -50:       # Out of bounds check
            self.active = False
            return False       # Flag a miss
        return True

    def draw(self, surface):
        points = []
        if self.lane == 0:    # Left
            points = [(self.x + self.size, self.y), (self.x, self.y + self.size//2), (self.x + self.size, self.y + self.size)]
        elif self.lane == 1:  # Down
            points = [(self.x, self.y), (self.x + self.size, self.y), (self.x + self.size//2, self.y + self.size)]
        elif self.lane == 2:  # Up
            points = [(self.x, self.y + self.size), (self.x + self.size, self.y + self.size), (self.x + self.size//2, self.y)]
        elif self.lane == 3:  # Right
            points = [(self.x, self.y), (self.x + self.size, self.y + self.size//2), (self.x, self.y + self.size)]
        
        pygame.draw.polygon(surface, self.color, points)

# Create arrow list
arrows = []

def reset_game():
    global score, streak, miss_count, game_over, arrows, spawn_timer, rating_text, rating_timer
    score = 0
    streak = 0
    miss_count = 0
    spawn_timer = 0
    rating_text = ""
    rating_timer = 0
    arrows.clear()
    game_over = False

# 7. Main Game Loop
running = True
while running:
    screen.fill(BLACK)
    
    # Check for game over state
    if miss_count >= MAX_MISSES:
        game_over = True

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_over:
                reset_game()

        elif event.type == pygame.KEYDOWN and not game_over:
            if event.key in KEY_MAP:
                pressed_lane = KEY_MAP[event.key]
                hit_registered = False
                
                # Check for closest arrow in that lane near STRUM_Y
                for arrow in arrows:
                    if arrow.lane == pressed_lane and arrow.active:
                        distance = abs(arrow.y - STRUM_Y)
                        
                        if distance < 60:  # Hit window
                            arrow.active = False
                            hit_registered = True
                            streak += 1
                            
                            # Determine accuracy rating based on timing distance
                            if distance < 15:
                                rating_text = "SICK!!"
                                rating_color = UP_G
                                score += 350
                            elif distance < 35:
                                rating_text = "GOOD"
                                rating_color = DOWN_B
                                score += 200
                            else:
                                rating_text = "BAD"
                                rating_color = RED
                                score += 50
                            rating_timer = 20  # Frame duration to display text
                            break
                
                if not hit_registered:
                    # Input penalty for ghost tapping / missing completely
                    rating_text = "MISS"
                    rating_color = RED
                    rating_timer = 20
                    streak = 0
                    miss_count += 1
                    score = max(0, score - 100)

    if not game_over:
        # DYNAMIC SPEED SYSTEM
        arrow_speed = min(16, BASE_SPEED + (score // 1500))
        
        # Proc-Gen Arrow Spawner
        spawn_timer += 1
        if spawn_timer >= SPAWN_RATE:
            if random.random() > 0.3:  # 70% chance to spawn an arrow on interval
                chosen_lane = random.choice(LANES)
                arrows.append(Arrow(chosen_lane))
            spawn_timer = 0

        # Draw Receptor Strums (Static Target Zones)
        for i in range(4):
            rect = pygame.Rect(LANE_X[i], STRUM_Y, 50, 50)
            keys_pressed = pygame.key.get_pressed()
            is_held = (i == 0 and keys_pressed[pygame.K_LEFT]) or \
                      (i == 1 and keys_pressed[pygame.K_DOWN]) or \
                      (i == 2 and keys_pressed[pygame.K_UP]) or \
                      (i == 3 and keys_pressed[pygame.K_RIGHT])
            
            color = LANE_COLORS[i] if is_held else GRAY
            pygame.draw.rect(screen, color, rect, width=3, border_radius=4)

        # Update and Draw Active Arrows
        for arrow in arrows[:]:
            if arrow.active:
                still_alive = arrow.update()
                if not still_alive:
                    # Registered as a natural scroll miss
                    rating_text = "MISS"
                    rating_color = RED
                    rating_timer = 20
                    streak = 0
                    miss_count += 1
                    score = max(0, score - 50)
                    arrows.remove(arrow)
                else:
                    arrow.draw(screen)
            else:
                arrows.remove(arrow)

        # Render Interface Metrics
        # Score, Speed, Combo & Misses Display
        txt_score = font_score.render(f"Score: {score}  |  Combo: {streak}  |  Misses: {miss_count}/{MAX_MISSES}", True, WHITE)
        screen.blit(txt_score, (20, 20))
        
        # Timing Judgement Text (SICK, GOOD, BAD, MISS)
        if rating_timer > 0:
            txt_rating = font_rating.render(rating_text, True, rating_color)
            text_rect = txt_rating.get_rect(center=(SCREEN_WIDTH // 2, STRUM_Y + 150))
            screen.blit(txt_rating, text_rect)
            rating_timer -= 1
            
    else:
        # --- GAME OVER SCREEN ---
        screen.fill((20, 10, 10)) # Slight dark red tint background
        
        go_surface = font_game_over.render("GAME OVER", True, RED)
        go_rect = go_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        
        score_surface = font_score.render(f"Final Score: {score}", True, WHITE)
        score_rect = score_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
        
        restart_surface = font_restart.render("Click Anywhere to Restart", True, DOWN_B)
        restart_rect = restart_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80))
        
        screen.blit(go_surface, go_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(restart_surface, restart_rect)

    # Update Frame and Sync
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
