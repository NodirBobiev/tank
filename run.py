import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Top-Down Tank Game')

# Colors
background_color = (0, 0, 0)  # Black
tank_main_color = (34, 139, 34)  # Forest green for the main tank body
tank_detail_color = (105, 105, 105)  # Dim gray for tank details (turret and wheels)

# Tank properties
tank_body_width, tank_body_height = 40, 60
tank_turret_width, tank_turret_height = 20, 5
tank_wheel_width, tank_wheel_height = 50, 10
tank_position = [screen_width // 2, screen_height // 2]
tank_speed = 5

def draw_tank(x, y):
    # Tank body
    pygame.draw.rect(screen, tank_main_color, (x, y, tank_body_width, tank_body_height))
    
    # Tank turret
    turret_x = x + (tank_body_width - tank_turret_width) // 2
    turret_y = y + (tank_body_height - tank_turret_width) // 2
    pygame.draw.rect(screen, tank_detail_color, (turret_x, turret_y - tank_turret_height * 2, tank_turret_width, tank_turret_height * 4))

    # Tank wheels - adjust as per design preference
    wheel_positions = [(x - 5, y + 10), (x + tank_body_width - tank_wheel_width + 55, y + 10),  # Top wheels
                       (x - 5, y + tank_body_height - 20), (x + tank_body_width - tank_wheel_width + 55, y + tank_body_height - 20)]  # Bottom wheels
    for wx, wy in wheel_positions:
        pygame.draw.rect(screen, tank_detail_color, (wx, wy, tank_wheel_width - 40, tank_wheel_height))

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key handling for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        tank_position[0] -= tank_speed
    if keys[pygame.K_RIGHT]:
        tank_position[0] += tank_speed
    if keys[pygame.K_UP]:
        tank_position[1] -= tank_speed
    if keys[pygame.K_DOWN]:
        tank_position[1] += tank_speed

    # Prevent the tank from going out of bounds
    tank_position[0] = max(0, min(screen_width - tank_body_width, tank_position[0]))
    tank_position[1] = max(0, min(screen_height - tank_body_height, tank_position[1]))

    # Fill the screen with the background color
    screen.fill(background_color)

    # Draw the tank
    draw_tank(*tank_position)

    # Update the display
    pygame.display.flip()

    # Cap the FPS
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
