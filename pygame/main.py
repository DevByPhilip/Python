import pygame

# Initialize Pygame
pygame.init()

# Create a display window
size = (1200, 1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (optional)
    screen.fill((0, 25, 255))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()