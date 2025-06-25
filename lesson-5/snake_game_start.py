""" Lesson 5: 

Objective
*********
Implement the snake as a class. This makes the code more readable and modular, and easier to extend in the future.

Note
****
When getting the x and y coordinates of the snake's head (which is a tuple), we unpack the tuple


Some refactoring has been done to prepare for this lesson.
In lesson 4, we saw that the snake_x and snake_y variables are "copies" of the values of the first (head) segment of the snake's body.
I have removed these variables and replaced them with functions that get the x and y coordinates of the snake's head from the snake's body.

I have create a KEY_DIRECTION_MAP dictionary to map the arrow keys to the direction of movement of the snake.
This allows us to change the direction of the snake based on key presses without using if statements.
This is very similar to the KEY_COLOUR_MAP dictionary we used in a previous lesson to change the colour of the snake.


Steps
*****
These are the steps to complete the code in this lesson:

Create the Snake class with the following attributes:
- body: a list of tuples representing the segments of the snake's body.
- colour: the colour of the snake.
- dx, dy: the current direction of movement of the snake. (for dx: -1 is left, 1 is right, for dy: -1 is up, 1 is down)

Implement the following methods in the Snake class:
* __init__: Initialize the snake's body, colour, position, and direction.
* __str__: Return a string representation of the snake's body and position, helpful for debugging
* move: Update the snake's position and body segments based on the current direction.
* is_out_of_bounds: Check if the snake's head is out of bounds of the board.

We want to keep the following as functions outside the class since they use pygame functions 
and we want to keep pygame-specific code separate from the Snake logic:
The snake variable will be an argument to these functions.
- draw_snake: Draw the snake on the screen.
- change_snake_direction: Change the direction of the snake based on key presses. It will alter the dx and dy attributes of the snake object.)
"""
import pygame

# Set up constants for colours.  Each colour is a tuple of red, green, blue  values.
COLOUR_GREEN = (0, 255, 0)
COLOUR_BLACK = (0, 0, 0)
COLOUR_BLUE = (0, 0, 255)
COLOUR_RED = (255, 0, 0)  
COLOUR_YELLOW = (255, 255, 0)
COLOUR_ORANGE = (255, 165, 0)

KEY_COLOUR_MAP = {
    pygame.K_b: COLOUR_BLUE,
    pygame.K_r: COLOUR_RED,
    pygame.K_y: COLOUR_YELLOW,
    pygame.K_g: COLOUR_GREEN,
    pygame.K_o: COLOUR_ORANGE
}

# refactored the direction keys in the same manner as the colours
KEY_DIRECTION_MAP = {
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0)
}

FRAME_RATE = 5  # Frames per second (FPS) for the game
# Set up "Chess board" squares geometry constants
SQUARE_SIZE = 20  # Size of each square in pixels
NUM_SQUARES_X = 32  # Number of squares in the x direction  
NUM_SQUARES_Y = 24  # Number of squares in the y direction
SCREEN_WIDTH = SQUARE_SIZE * NUM_SQUARES_X
SCREEN_HEIGHT = SQUARE_SIZE * NUM_SQUARES_Y

# Set up initial position and movement variables for the snake
snake_dx = 1  # Change in x (horizontal movement)
snake_dy = 0  # Change in y (vertical movement)

# Implement the snake as a list of tuples representing its body segments
snake_body = []  # Initialize the snake body as an empty list
for i in range(3):
    snake_body.append((NUM_SQUARES_X // 2 - i, NUM_SQUARES_Y // 2))  # Add segments to the left of the head

print(f"Initial snake position: {snake_body}")
snake_colour = COLOUR_GREEN  # Default colour for the snake

# These functions will become methods of the Snake class

def is_snake_out_of_bounds(snake_body):
    """Check if the snake's head is out of bounds of the screen."""
    x_pos, y_pos = snake_body[0]
    return (x_pos < 0 or x_pos >= NUM_SQUARES_X or 
            y_pos < 0 or y_pos >= NUM_SQUARES_Y)

def move_snake(snake_dx, snake_dy, snake_body):
    """Update the snake's position and body segments based on the current direction"""
    old_head_x, old_head_y = snake_body[0]  
    new_head = (old_head_x + snake_dx, old_head_y + snake_dy)
    snake_body.insert(0, new_head)
    snake_body.pop()
    return snake_body

# These functions will pass in the snake variable as an argument

def draw_snake(SQUARE_SIZE, snake_body, snake_colour, screen):
    """Draw the snake on the screen as a series of rectangles."""
    for segment in snake_body:
        pygame.draw.rect(screen, snake_colour, [segment[0]*SQUARE_SIZE, segment[1]*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE])

def change_snake_direction(current_dx, current_dy, event):
    """Change the direction of the snake based on key presses."""
    if event.key not in KEY_DIRECTION_MAP:
        return current_dx, current_dy  # If the key is not a direction key, return the current direction    
    # Get the new direction from the KEY_DIRECTION_MAP    
    new_dx, new_dy = KEY_DIRECTION_MAP[event.key]    
    # Prevent the snake from turning back on itself 
    if not (current_dx, current_dy) == (-new_dx, -new_dy):
        current_dx, current_dy = new_dx, new_dy        
    return current_dx, current_dy

# Initialize Pygame, and the mixer module (which is used for sound)
pygame.init()
pygame.mixer.init()  

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Create the game window
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
                snake_colour = KEY_COLOUR_MAP[event.key]
                print(f"Colour changed to {snake_colour}")

            # Set dx and dy values based on the arrow keys pressed
            snake_dx, snake_dy = change_snake_direction(snake_dx, snake_dy, event)
            
    # Check if the snake is out of bounds
    if is_snake_out_of_bounds(snake_body):
        print("Game Over! The snake has gone out of bounds.")
        game_over = True
        continue

    # Update the snake's position based on the current direction
    snake_body = move_snake(snake_dx, snake_dy, snake_body)

    # Fill the background with black
    screen.fill(COLOUR_BLACK)

    # Draw the snake as a set of rectangles for each segment
    draw_snake(SQUARE_SIZE, snake_body, snake_colour, screen)

    pygame.display.update()  
    clock.tick(FRAME_RATE)

pygame.quit()
