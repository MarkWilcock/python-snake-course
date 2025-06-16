"""
Lesson 4: 

Objectives
The snake moves properly at a constant speed and cannot turn back on itself.  
The game is over when the snake moves off the screen.

Steps
1. Improve the geometry so that the snake is defined in terms of squares on a chess board (but one that has more than 8 by 8 squares).
2. Detect when the snake moves off the chess board / screen and end the game.
3. The snake moves at a constant speed in the direction of the arrow keys.
4. The snake cannot turn back on itself.  It cannot start moving in the opposite direction immediately.
"""

import pygame

FRAME_RATE = 5  # Frames per second (FPS) for the game

# TO DO: Set up "Chess board" squares geometry constants
SQUARE_SIZE = 20  # Size of each square in pixels
NUM_SQUARES_X = 32  # Number of squares in the x direction  
NUM_SQUARES_Y = 24  # Number of squares in the y direction
# Calculate the width and height of the screen based on the number of squares and square size
SCREEN_WIDTH = SQUARE_SIZE * NUM_SQUARES_X
SCREEN_HEIGHT = SQUARE_SIZE * NUM_SQUARES_Y

# TO DO: Set up initial position and movement variables for the snake
snake_x = SCREEN_WIDTH / 2  # Start in the middle of the screen
snake_y = SCREEN_HEIGHT / 2  # Start in the middle of the screen
dx = 0  # Change in x (horizontal movement)
dy = 0  # Change in y (vertical movement)

# TO DO: Implement the snake as a list of tuples representing its body segments
snake = [(snake_x, snake_y), (snake_x-SQUARE_SIZE, snake_y), (snake_x-2*SQUARE_SIZE, snake_y)]  # Start with one segment at the initial position

print(f"Initial snake position: {snake}")

# Set up constants for colours.  Each colour is a tuple of red, green, blue  values.  Each value can range from 0 to 255.
COLOUR_GREEN = (0, 255, 0)
COLOUR_BLACK = (0, 0, 0)
COLOUR_BLUE = (0, 0, 255)
COLOUR_RED = (255, 0, 0)  
COLOUR_YELLOW = (255, 255, 0)
COLOUR_ORANGE = (255, 165, 0)

# TO DO: add the KEY_COLOUR_MAP dictionary
KEY_COLOUR_MAP = {
    pygame.K_b: COLOUR_BLUE,
    pygame.K_r: COLOUR_RED,
    pygame.K_y: COLOUR_YELLOW,
    pygame.K_g: COLOUR_GREEN,
    pygame.K_o: COLOUR_ORANGE
}

colour = COLOUR_GREEN  # Default colour for the snake

# Initialize Pygame, and the mixer module (which is used for sound)
pygame.init()
pygame.mixer.init()  

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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
            if event.key in KEY_COLOUR_MAP:
                colour = KEY_COLOUR_MAP[event.key]
                print(f"Colour changed to {colour}")

            # TO DO: Set dx and dy values based on the arrow keys pressed
            dx = 0
            dy = 0
            if event.key == pygame.K_UP:
                dy = -SQUARE_SIZE
            elif event.key == pygame.K_DOWN:
                dy = SQUARE_SIZE
            elif event.key == pygame.K_LEFT:
                dx = -SQUARE_SIZE
            elif event.key == pygame.K_RIGHT:
                dx = SQUARE_SIZE

            # TO DO: Update the snake's position based on the current direction
            if dx != 0 or dy != 0:
                snake_x += dx
                snake_y += dy
                new_snake_head = (snake_x, snake_y)
                snake.insert(0, new_snake_head)
                snake.pop()
            
    # Fill the background with black
    screen.fill(COLOUR_BLACK)

    # TO DO: Draw the snake as a set of rectangles for each segment

    for segment in snake:
        pygame.draw.rect(screen, colour, [segment[0], segment[1], SQUARE_SIZE,SQUARE_SIZE])

    pygame.display.update()

    # Limit the frame rate to 5 frames per second (FPS)
    clock.tick(FRAME_RATE)

pygame.quit()
