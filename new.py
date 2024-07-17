import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the width and height of the window
width = 800
height = 600

# Create the Pygame display surface
screen = pygame.display.set_mode((width, height))

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()