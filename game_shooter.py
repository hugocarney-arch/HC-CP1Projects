import math
import random
import pygame

# Initialize Game
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3rd Person Shooter Engine")
clock = pygame.time.Clock()

# Colors
GREEN = (34, 139, 34)
DARK_GREEN = (20, 100, 20)
BLUE = (50, 100, 240)
RED = (220, 40, 40)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Game Variables
player_x, player_y = 0.0, 0.0
player_angle = 0.0  # Direction player faces
cam_angle = 0.0     # Camera orbit rotation angle
score = 0

# Laser line mechanics
laser_timer = 0
laser_start = (0, 0)
laser_end = (0, 0)

class Bot:
    def __init__(self):
        self.spawn()
        
    def spawn(self):
        # Spawn somewhere in the distance relative to player
        self.x = player_x + random.uniform(-400, 400)
        self.y = player_y + random.uniform(200, 500)
        self.radius = 20

bots = [Bot() for _ in range(5)]

# Mouse lock setup
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

running = True
while running:
    clock.tick(60)
    screen.fill((135, 206, 235)) # Sky Blue background

    # 1. Handle Window and Input Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
            
        # Left Click to shoot ahead of character
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            laser_timer = 5
            # Fire vector along the direction the player is looking
            look_x = math.sin(player_angle)
            look_y = math.cos(player_angle)
            
            # Check hits against bots
            for bot in bots:
                # Vector from player to bot
                bx = bot.x - player_x
                by = bot.y - player_y
                
                # Projection to see how close bot is to laser beam line
                dot = bx * look_x + by * look_y
                if dot > 0: # Bot is in front of player orientation
                    closest_x = player_x + look_x * dot
                    closest_y = player_y + look_y * dot
                    dist = math.hypot(bot.x - closest_x, bot.y - closest_y)
                    
                    if dist < bot.radius + 15: # Hit validation check
                        score += 100
                        bot.spawn()
                        break

    # 2. Camera Orbit Tracking via Mouse Movement
    mx, my = pygame.mouse.get_rel()
    cam_angle += mx * 0.005
    player_angle = cam_angle # Lock player direction orientation to view lens

    # 3. Handle Keyboard Movement (WASD Matrix)
    keys = pygame.key.get_pressed()
    speed = 4.0
    dx, dy = 0, 0
    
    if keys[pygame.K_w]:
        dx += math.sin(player_angle) * speed
        dy += math.cos(player_angle) * speed
    if keys[pygame.K_s]:
        dx -= math.sin(player_angle) * speed
        dy -= math.cos(player_angle) * speed
    if keys[pygame.K_a]:
        dx -= math.cos(player_angle) * speed
        dy += math.sin(player_angle) * speed
    if keys[pygame.K_d]:
        dx += math.cos(player_angle) * speed
        dy -= math.sin(player_angle) * speed

    player_x += dx
    player_y += dy

    # 4. Render Ground Floor Plane Grid perspective from behind
    # Horizon divider position line
    horizon = 250 
    pygame.draw.rect(screen, GREEN, (0, horizon, WIDTH, HEIGHT - horizon))
    
    # Draw field landscape guide tracks to simulate moving camera depth
    for i in range(-10, 11):
        line_x_world = (i * 100) - (player_x % 100)
        # Perspective transform back map coords into screen coordinates space
        screen_x_start = int(WIDTH / 2 + line_x_world)
        pygame.draw.line(screen, DARK_GREEN, (screen_x_start, horizon), (screen_x_start + int(i * 50), HEIGHT), 2)

    # 5. Render Bots Relative to 3rd-Person Camera Matrix Viewport
    for bot in bots:
        # Move bots slowly towards player position track
        angle_to_player = math.atan2(player_y - bot.y, player_x - bot.x)
        bot.x += math.cos(angle_to_player) * 1.5
        bot.y += math.sin(angle_to_player) * 1.5
        
        # Translate to screen perspective coordinates
        rel_x = bot.x - player_x
        rel_y = bot.y - player_y
        
        # Unwind rotation offset to fix position behind view tracking lens
        rot_x = rel_x * math.cos(-cam_angle) - rel_y * math.sin(-cam_angle)
        rot_y = rel_x * math.sin(-cam_angle) + rel_y * math.cos(-cam_angle)
        
        if rot_y > 10: # Only draw bot if it's forward/ahead of screen plane horizon
            screen_x = int(WIDTH / 2 + (rot_x * 200 / rot_y))
            screen_y = int(horizon + (20000 / rot_y))
            size = max(4, min(100, int(bot.radius * 200 / rot_y)))
            
            if 0 < screen_x < WIDTH and horizon < screen_y < HEIGHT:
                pygame.draw.ellipse(screen, RED, (screen_x - size//2, screen_y - size, size, size))

    # 6. Draw Player Character Model (Locked centered in 3rd Person Viewpoint)
    # Placed centrally slightly below horizon line looking out forward
    player_screen_x = WIDTH // 2
    player_screen_y = HEIGHT - 150
    pygame.draw.rect(screen, BLUE, (player_screen_x - 15, player_screen_y, 30, 60))
    pygame.draw.circle(screen, WHITE, (player_screen_x, player_screen_y - 15), 12) # Head asset 

    # Render shot indicator laser ray beam trace path
    if laser_timer > 0:
        pygame.draw.line(screen, YELLOW, (player_screen_x, player_screen_y + 10), (player_screen_x, horizon), 4)
        laser_timer -= 1

    # Static crosshair position overlay
    pygame.draw.circle(screen, RED, (WIDTH // 2, horizon + 50), 4)

    # Score Tracker UI
    font = pygame.font.SysFont('Arial', 24)
    text = font.render(f"SCORE: {score}", True, WHITE)
    screen.blit(text, (20, 20))

    pygame.display.flip()

pygame.quit()
