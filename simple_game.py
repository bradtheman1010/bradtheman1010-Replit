import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Pygame Test")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(black)
    pygame.draw.rect(screen, white, (350, 250, 100, 100))  # Draw a white square
    pygame.display.flip()  # Update the display
