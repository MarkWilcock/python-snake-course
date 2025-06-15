"""
Lesson 3: 

Step: Implement the key to colour mapping as a dictionary.

Step: Make the snake move by pressing the arrow keys

Step: Create a better geometry for the screen based on square size and number of squares.


"""

import pygame

# Set up constants for colours
# Each colour is a tuple of red, green, blue  values.  Each value can range from 0 to 255.
COLOUR_GREEN = (0, 255, 0)
COLOUR_BLACK = (0, 0, 0)
COLOUR_BLUE = (0, 0, 255)
COLOUR_RED = (255, 0, 0)  
COLOUR_YELLOW = (255, 255, 0)
COLOUR_ORANGE = (255, 165, 0)

colour = COLOUR_GREEN  # Default colour for the snake

# Initialize Pygame
pygame.init()
# Initialize the mixer module (which is used for sound)
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
        print(event)

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
            
    # Fill the background with black
    screen.fill(COLOUR_BLACK)

    # Draw a COLOUR_GREEN square (the snake) at the center of the screen
    # The square is 20x20 pixels in size and is drawn at (320, 240) on the screen.
    # The coordinates are the top-left corner of the square.
    pygame.draw.rect(screen, colour, [320, 240, 20,20])

    pygame.display.update()

    # Limit the frame rate to 5 frames per second (FPS)
    clock.tick(5)

pygame.quit()
