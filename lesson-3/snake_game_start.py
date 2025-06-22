"""
Lesson 3: The snake moves and looks more like a snake!

Steps
1. Implement the key to colour mapping as a dictionary.
2. Create a better geometry for the screen based on square size and number of squares.
3. Make the snake move by pressing the arrow keys
4. Implement the snake as a list of tuples representing its body segments.
"""

import pygame

# TO DO: Set up "Chess board" squares geometry constants

# TO DO: Set up initial position and movement variables for the snake

# TO DO: Implement the snake as a list of tuples representing its body segments

# Set up constants for colours.  Each colour is a tuple of red, green, blue  values.  Each value can range from 0 to 255.
COLOUR_GREEN = (0, 255, 0)
COLOUR_BLACK = (0, 0, 0)
COLOUR_BLUE = (0, 0, 255)
COLOUR_RED = (255, 0, 0)  
COLOUR_YELLOW = (255, 255, 0)
COLOUR_ORANGE = (255, 165, 0)

# TO DO: add the KEY_COLOUR_MAP dictionary

colour = COLOUR_GREEN  # Default colour for the snake

# Initialize Pygame, and the mixer module (which is used for sound)
pygame.init()
pygame.mixer.init()  

# Create the game window
screen = pygame.display.set_mode((640, 480))

# Set the title of the window
pygame.display.set_caption("Python Snake Game")

clock = pygame.time.Clock()

game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        # Print the event to see what events are being generated
        # print(event)

        if event.type == pygame.KEYDOWN:
            # Check which key was pressed
            if event.key == pygame.K_b:
                colour = COLOUR_BLUE
            elif event.key == pygame.K_r:
                colour = COLOUR_RED
            elif event.key == pygame.K_y:
                colour = COLOUR_YELLOW
            elif event.key == pygame.K_g:
                colour = COLOUR_GREEN
            elif event.key == pygame.K_o:
                colour = COLOUR_ORANGE

            # TO DO: Set snake_dx and snake_dy values based on the arrow keys pressed

            # TO DO: Update the snake's position based on the current direction
            
    # Fill the background with black
    screen.fill(COLOUR_BLACK)

    # TO DO: Draw the snake as a set of rectangles for each segment

    pygame.draw.rect(screen, colour, [320, 240, 20,20])

    pygame.display.update()

    # Limit the frame rate to 5 frames per second (FPS)
    clock.tick(5)

pygame.quit()
