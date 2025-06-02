# The pygame library is used to create games in Python.
# It provides functions to create windows, draw shapes, handle events, and play sounds.
import pygame

"""
This is the initial starting point to build the snake game.
It has the minimal boiler-plate pygame code to get started.
It will draw a COLOUR_GREEN square on a black background and wait for 2 seconds before quitting.
"""
# Set up constants for colours
# Each colour is a tuple of COLOUR_RED, COLOUR_GREEN,  Blue  values.  Each value can range from 0 to 255.
COLOUR_GREEN = (0, 255, 0)
COLOUR_BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()
# Initialize the mixer module (which is used for sound)
pygame.mixer.init()  

# Create the game window
screen = pygame.display.set_mode((640, 480))

# Set the title of the window
pygame.display.set_caption("Python Snake Game")

# Fill the background with black
screen.fill(COLOUR_BLACK)

# Draw a COLOUR_GREEN square (the snake) at the center of the screen
# The square is 20x20 pixels in size and is drawn at (320, 240) on the screen.
# The coordinates are the top-left corner of the square.
pygame.draw.rect(screen, COLOUR_GREEN, [320, 240, 20,20])

pygame.display.update()

# Wait for 2 seconds to see the drawn square
# This is just to keep the window open for a while before quitting.
pygame.time.delay(10000)

pygame.quit()