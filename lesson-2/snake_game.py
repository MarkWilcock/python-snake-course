"""
Lesson 2: These are the changes to create the game loop 

step 1: add a pygame clock to control the frame rate
clock = pygame.time.Clock() # put just before the game loop starts

step 2: add a while loop to keep the game running
game_over = False
while not game_over:
    ...
    clock.tick(5) # Limit the frame rate to 5 frames per second (FPS)

step 3: add an event loop to handle user input and quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    

step 4: print each event to see what events are being generated
We'll see that the games is "listening" to and identifying our keyboard presses and mouse movements.

step 5: add a few more colour constants
COLOUR_BLUE = (0, 0, 255)
COLOUR_RED = (255, 0, 0)  
COLOUR_YELLOW = (255, 255, 0)
COLOUR_ORANGE = (255, 165, 0)

step 6: listen for the keydown event, check the key pressed and change the colour of the snake based on thse rules:
    B -> blue
    R -> red
    Y -> yellow
    G -> green
    O -> orange

"""

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

# Wait for 5 seconds to see the drawn square
# This is just to keep the window open for a while before quitting.
pygame.time.delay(5000)

pygame.quit()
