import pygame
import random
import math

# Initialize pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
BACKGROUND_COLOR = (34, 139, 34)  # Grass green
PLAYER_COLOR = (0, 0, 255)      # Blue character
ENEMY_COLOR = (255, 0, 0)       # Red enemy
BULLET_COLOR = (255, 215, 0)    # Gold ammunition
TEXT_COLOR = (255, 255, 255)

# Setup Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Battle Royale Shooter")
clock = pygame.time.Clock()

# Entities Classes
class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.radius = 20
        self.speed = 5
        self.health = 100

    def move(self, keys):
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.y += self.speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x += self.speed
        
        # Keep inside screens borders
        self.x = max(self.radius, min(SCREEN_WIDTH - self.radius, self.x))
        self.y = max(self.radius, min(SCREEN_HEIGHT - self.radius, self.y))

    def draw(self, surface):
        pygame.draw.circle(surface, PLAYER_COLOR, (self.x, self.y), self.radius)

class Bullet:
    def __init__(self, start_x, start_y, target_x, target_y):
        self.x = start_x
        self.y = start_y
        self.radius = 5
        self.speed = 10
        
        # Calculate angle and velocity vectors toward mouse pointer
        angle = math.atan2(target_y - start_y, target_x - start_x)
        self.dx = math.cos(angle) * self.speed
        self.dy = math.sin(angle) * self.speed

    def update(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self, surface):
        pygame.draw.circle(surface, BULLET_COLOR, (int(self.x), int(self.y)), self.radius)

class Enemy:
    def __init__(self):
        self.radius = 15
        self.speed = random.uniform(1.5, 3.5)
        self.health = 1
        
        # Spawn outside the visible canvas randomly
        if random.choice([True, False]):
            self.x = random.choice([-50, SCREEN_WIDTH + 50])
            self.y = random.randint(0, SCREEN_HEIGHT)
        else:
            self.x = random.randint(0, SCREEN_WIDTH)
            self.y = random.choice([-50, SCREEN_HEIGHT + 50])

    def update(self, player_x, player_y):
        # Tracking algorithm to chase the player
        angle = math.atan2(player_y - self.y, player_x - self.x)
        self.x += math.cos(angle) * self.speed
        self.y += math.sin(angle) * self.speed

    def draw(self, surface):
        pygame.draw.circle(surface, ENEMY_COLOR, (int(self.x), int(self.y)), self.radius)

# Game initialization variables
player = Player()
bullets = []
enemies = []
score = 0
font = pygame.font.SysFont("Arial", 24)

# Enemy spawning timer setup
SPAWN_ENEMY_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_ENEMY_EVENT, 1000) # Spawns every 1 second

# Main Loop Execution
running = True
game_over = False

while running:
    clock.tick(FPS)
    screen.fill(BACKGROUND_COLOR)

    # Event Framework handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == SPAWN_ENEMY_EVENT and not game_over:
            enemies.append(Enemy())
            
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            if event.button == 1: # Left Mouse Click
                mouse_x, mouse_y = pygame.mouse.get_pos()
                bullets.append(Bullet(player.x, player.y, mouse_x, mouse_y))

    if not game_over:
        # Check keystrokes
        keys = pygame.key.get_pressed()
        player.move(keys)

        # Update Projectiles
        for bullet in bullets[:]:
            bullet.update()
            # Delete if off screen bounds
            if bullet.x < 0 or bullet.x > SCREEN_WIDTH or bullet.y < 0 or bullet.y > SCREEN_HEIGHT:
                bullets.remove(bullet)

        # Update and Process Threats
        for enemy in enemies[:]:
            enemy.update(player.x, player.y)

            # Hit-detection: Enemy hits Player
            distance_to_player = math.hypot(player.x - enemy.x, player.y - enemy.y)
            if distance_to_player < player.radius + enemy.radius:
                player.health -= 10
                enemies.remove(enemy)
                if player.health <= 0:
                    game_over = True

            # Hit-detection: Bullet hits Enemy
            for bullet in bullets[:]:
                distance_to_bullet = math.hypot(bullet.x - enemy.x, bullet.y - enemy.y)
                if distance_to_bullet < bullet.radius + enemy.radius:
                    if bullet in bullets:
                        bullets.remove(bullet)
                    if enemy in enemies:
                        enemies.remove(enemy)
                    score += 1
                    break

    # Rendering Scene
    player.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)

    # Draw User Interface text layouts
    score_text = font.render(f"Eliminations: {score}", True, TEXT_COLOR)
    health_text = font.render(f"HP: {player.health}", True, TEXT_COLOR)
    screen.blit(score_text, (10, 10))
    screen.blit(health_text, (10, 40))

    if game_over:
        game_over_text = font.render("ELIMINATED! Game Over.", True, (255, 0, 0))
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2))

    pygame.display.flip()

pygame.quit()
