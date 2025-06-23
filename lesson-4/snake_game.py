""" Lesson 4: 

Objectives
* The snake moves properly at a constant speed and cannot turn back on itself.  
* The game is over when the snake moves off the screen.

Done
* Renamed snake to snake_body since it is only one aspect of the snake's state.
* Refactor the colour, dx, dy variables to prepend with snake_ to indicate they are part of the snake's state.

These are the steps to complete the code:

Use integer division (//) to calculate the position of the snake on the chess board.

Improve the geometry so that the snake is defined in terms of squares co-ordinates.
- remove SQUARE_SIZE factor when creating the snake_body, snake_dx_snake_dy
- remove SQUARE_SIZE factor when updating the snake position
- add in SQUARE_SIZE factor when drawing the snake segments.

Create the snake_body in a for loop to initialize it with three segments.

Change the snake's movement so that it moves at a constant speed in the direction of the arrow keys
In the event loop
* remove the lines to reset snake_dx, snake_dy to 0 
* in the if statement, set both snake_dx, snake_dy  on same line
* move the code block to update the snake position to the while loop, so it is executed once per frame.

Add guard test so that snake cannot turn back on itself i.e. it cannot start moving in the opposite direction immediately.

Write functions and refactor the code to make it more modular and easier to read.
* draw_snake
* change_snake_direction

Detect when the snake moves off the screen and end the game.
Write function is_snake_out_of_bounds
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
FRAME_RATE = 20  # Frames per second (FPS) for the game
# Set up "Chess board" squares geometry constants
SQUARE_SIZE = 20  # Size of each square in pixels
NUM_SQUARES_X = 32  # Number of squares in the x direction  
NUM_SQUARES_Y = 24  # Number of squares in the y direction
SCREEN_WIDTH = SQUARE_SIZE * NUM_SQUARES_X
SCREEN_HEIGHT = SQUARE_SIZE * NUM_SQUARES_Y

# Set up initial position and movement variables for the snake
snake_x = NUM_SQUARES_X // 2  # Start in the middle of the screen
snake_y = NUM_SQUARES_Y // 2  # Start in the middle of the screen
snake_dx = 1  # Change in x (horizontal movement)
snake_dy = 0  # Change in y (vertical movement)

# TO DO: Implement the snake as a list of tuples representing its body segments
snake_body = []  # Initialize the snake body as an empty list
for i in range(3):
    snake_body.append((snake_x - i, snake_y))  # Add segments to the left of the head

#[(snake_x, snake_y), (snake_x-SQUARE_SIZE, snake_y), (snake_x-2*SQUARE_SIZE, snake_y)]  # Start with one segment at the initial position
print(f"Initial snake position: {snake_body}")
snake_colour = COLOUR_GREEN  # Default colour for the snake

# Functions

def draw_snake(SQUARE_SIZE, snake_body, snake_colour, screen):
    for segment in snake_body:
        pygame.draw.rect(screen, snake_colour, [segment[0]*SQUARE_SIZE, segment[1]*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE])

def change_direction(snake_dx, snake_dy, event):
    if event.key == pygame.K_UP and not (snake_dx, snake_dy) == (0, 1):  # Prevent turning back on itself
        snake_dx, snake_dy = 0, -1
    elif event.key == pygame.K_DOWN and not (snake_dx, snake_dy) == (0, -1):
        snake_dx, snake_dy = 0, 1
    elif event.key == pygame.K_LEFT and not (snake_dx, snake_dy) == (1, 0):  # Prevent turning back on itself
        snake_dx, snake_dy = -1, 0
    elif event.key == pygame.K_RIGHT and not (snake_dx, snake_dy) == (-1, 0):
        snake_dx, snake_dy = 1, 0
    return snake_dx,snake_dy

def is_snake_out_of_bounds(snake_x, snake_y):
    """Check if the snake's head is out of bounds of the screen."""
    return (snake_x < 0 or snake_x >= NUM_SQUARES_X or
            snake_y < 0 or snake_y >= NUM_SQUARES_Y)


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
            snake_dx, snake_dy = change_direction(snake_dx, snake_dy, event)
            
    # Check if the snake is out of bounds
    if is_snake_out_of_bounds(snake_x, snake_y):
        print("Game Over! The snake has gone out of bounds.")
        game_over = True
        continue

    # Update the snake's position based on the current direction
    def move_snake(snake_x, snake_y, snake_dx, snake_dy, snake_body):
        """Update the snake's position and body segments."""
        snake_x += snake_dx
        snake_y += snake_dy
        new_snake_head = (snake_x, snake_y)
        snake_body.insert(0, new_snake_head)
        snake_body.pop()
        return snake_x, snake_y

    # Update the snake's position based on the current direction
    snake_x, snake_y = move_snake(snake_x, snake_y, snake_dx, snake_dy, snake_body)
            
    # Fill the background with black
    screen.fill(COLOUR_BLACK)

    # Draw the snake as a set of rectangles for each segment
    draw_snake(SQUARE_SIZE, snake_body, snake_colour, screen)

    pygame.display.update()  
    clock.tick(FRAME_RATE)

pygame.quit()
