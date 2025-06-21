""" Lesson 4: 

Objectives
* The snake moves properly at a constant speed and cannot turn back on itself.  
* The game is over when the snake moves off the screen.

Done
Renamed snake to snake_body since it is only one aspect of the snake's state.
Refactor the colour, dx, dy variables to prepend with snake_ to indicate they are part of the snake's state.

Steps

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

Detect when the snake moves off the screen and end the game.

Write functions and refactor the code to make it more modular and easier to read.
* draw_snake
* change_snake_direction
* change_snake_colour
* is_snake_out_of_bounds

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
FRAME_RATE = 5  # Frames per second (FPS) for the game
# Set up "Chess board" squares geometry constants
SQUARE_SIZE = 20  # Size of each square in pixels
NUM_SQUARES_X = 32  # Number of squares in the x direction  
NUM_SQUARES_Y = 24  # Number of squares in the y direction
SCREEN_WIDTH = SQUARE_SIZE * NUM_SQUARES_X
SCREEN_HEIGHT = SQUARE_SIZE * NUM_SQUARES_Y

# Set up initial position and movement variables for the snake
snake_x = SCREEN_WIDTH / 2  # Start in the middle of the screen
snake_y = SCREEN_HEIGHT / 2  # Start in the middle of the screen
snake_dx = 0  # Change in x (horizontal movement)
snake_dy = 0  # Change in y (vertical movement)

# TO DO: Implement the snake as a list of tuples representing its body segments
snake_body = [(snake_x, snake_y), (snake_x-SQUARE_SIZE, snake_y), (snake_x-2*SQUARE_SIZE, snake_y)]  # Start with one segment at the initial position
print(f"Initial snake position: {snake_body}")
snake_colour = COLOUR_GREEN  # Default colour for the snake

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
            snake_dx = 0
            snake_dy = 0
            if event.key == pygame.K_UP:
                snake_dy = -SQUARE_SIZE
            elif event.key == pygame.K_DOWN:
                snake_dy = SQUARE_SIZE
            elif event.key == pygame.K_LEFT:
                snake_dx = -SQUARE_SIZE
            elif event.key == pygame.K_RIGHT:
                snake_dx = SQUARE_SIZE

            # Update the snake's position based on the current direction
            if snake_dx != 0 or snake_dy != 0:
                snake_x += snake_dx
                snake_y += snake_dy
                new_snake_head = (snake_x, snake_y)
                snake_body.insert(0, new_snake_head)
                snake_body.pop()
            
    # Fill the background with black
    screen.fill(COLOUR_BLACK)

    # Draw the snake as a set of rectangles for each segment
    for segment in snake_body:
        pygame.draw.rect(screen, snake_colour, [segment[0], segment[1], SQUARE_SIZE, SQUARE_SIZE])

    pygame.display.update()  
    clock.tick(FRAME_RATE)

pygame.quit()
