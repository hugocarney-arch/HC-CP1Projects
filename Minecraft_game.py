from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# Initialize the game engine
app = Ursina()

# Define types of blocks with different colors
BLOCK_TYPES = {
    '1': color.rgb(40, 180, 99),   # Grass (Green)
    '2': color.rgb(139, 69, 19),   # Dirt (Brown)
    '3': color.rgb(128, 128, 128), # Stone (Grey)
    '4': color.rgb(241, 196, 15)   # Gold (Yellow)
}

current_block_type = '1'

# Handle keyboard inputs for choosing blocks or exiting
def input(key):
    global current_block_type
    if key in BLOCK_TYPES:
        current_block_type = key
        print(f"Selected block type: {key}")
    if key == 'escape':
        quit()

# Create a Voxel (Block) class
class Voxel(Button):
    def __init__(self, position=(0,0,0), block_color=color.white):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture='white_cube', # Built-in texture
            color=block_color,
            highlight_color=color.lime
        )

    # Handle placing and breaking blocks
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                # Create a new block adjacent to the clicked face
                Voxel(position=self.position + mouse.normal, block_color=BLOCK_TYPES[current_block_type])
            
            if key == 'right mouse down':
                # Destroy the block
                destroy(self)

# Generate a flat floor grid (15x15) to start building on
for z in range(15):
    for x in range(15):
        voxel = Voxel(position=(x, 0, z), block_color=BLOCK_TYPES['1'])

# Add the player (First Person Controls)
player = FirstPersonController()

# Run the game loop
app.run()
