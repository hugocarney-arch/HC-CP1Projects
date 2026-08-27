import random
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# Initialize the Ursina App
app = Ursina()

# Window Configuration for Retro/SD Feel
window.title = "Fortnite SD FPS"
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True

# --- Environment Setup ---
# The Ground (Grass Landscape)
ground = Entity(
    model='plane',
    scale=(100, 1, 100),
    color=color.green,
    texture='white_cube',
    texture_scale=(50, 50),
    collider='box'
)

# Random Wood Barricades (Fortnite Structure Vibes)
barricades = []
for _ in range(20):
    bx = random.uniform(-40, 40)
    bz = random.uniform(-40, 40)
    barricade = Entity(
        model='cube',
        position=(bx, 1.5, bz),
        scale=(random.uniform(2, 5), random.uniform(2, 4), 0.5),
        rotation_y=random.uniform(0, 360),
        color=color.orange,
        texture='white_cube',
        collider='box'
    )
    barricades.append(barricade)

# Skybox
Sky()

# --- Player & UI Setup ---
# First Person Controller
player = FirstPersonController()
player.y = 2
player.cursor.visible = False

# Crosshair UI
crosshair = Entity(
    parent=camera.ui,
    model='quad',
    color=color.red,
    scale=(0.02, 0.02)
)

# Player Health State
player_health = 100
health_text = Text(
    text=f"HP: {player_health}",
    position=(-0.85, 0.45),
    scale=2,
    color=color.green
)

# Score Tracker
eliminations = 0
score_text = Text(
    text=f"Eliminations: {eliminations}",
    position=(-0.85, 0.40),
    scale=1.5,
    color=color.yellow
)

# --- Weapon Creation ---
gun = Entity(
    parent=camera,
    model='cube',
    color=color.gold,
    position=(0.5, -0.4, 0.8),
    scale=(0.1, 0.15, 0.6),
    origin_z=-0.5
)

# --- Enemy Management ---
enemies = []

class TargetEnemy(Entity):
    def __init__(self, position):
        super().__init__(
            model='cube',
            color=color.magenta,
            texture='white_cube',
            position=position,
            scale=(1.2, 2, 1.2),
            collider='box'
        )
        self.speed = 3
        self.health = 2

    def update(self):
        # Move towards the player coordinates
        direction = (player.position - self.position).normalized()
        self.position += direction * self.speed * time.dt
        
        # Look flatly towards the player orientation
        self.look_at(player.position)
        self.rotation_x = 0
        self.rotation_z = 0

        # Physical contact damage calculation
        if distance(self.position, player.position) < 1.5:
            global player_health
            player_health -= 10 * time.dt
            health_text.text = f"HP: {int(player_health)}"
            
            # Simple game over check
            if player_health <= 0:
                health_text.text = "GAME OVER"
                print("Game Over! Restart to try again.")
                application.quit()

# Spawn initial wave of targets
def spawn_enemy():
    ex = random.uniform(-30, 30)
    ez = random.uniform(-30, 30)
    while distance((ex, 0, ez), player.position) < 10:
        ex = random.uniform(-30, 30)
        ez = random.uniform(-30, 30)
    
    new_enemy = TargetEnemy(position=(ex, 1, ez))
    enemies.append(new_enemy)

for _ in range(5):
    spawn_enemy()

# --- Game Loops & Input Mapping ---
def input(key):
    global eliminations
    
    # Click to Shoot mapping
    if key == 'left mouse down':
        gun.position = (0.5, -0.3, 0.6)
        gun.animate_position((0.5, -0.4, 0.8), duration=0.1)
        
        # Raycasting detection from viewport camera center
        hit_info = raycast(camera.world_position, camera.forward, distance=50)
        
        if hit_info.hit and hit_info.entity in enemies:
            enemy_hit = hit_info.entity
            enemy_hit.health -= 1
            enemy_hit.blink(color.red, duration=0.1)
            
            if enemy_hit.health <= 0:
                enemies.remove(enemy_hit)
                destroy(enemy_hit)
                eliminations += 1
                score_text.text = f"Eliminations: {eliminations}"
                spawn_enemy()

# Run the app engine
app.run()
