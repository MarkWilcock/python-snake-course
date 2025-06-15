"""
Lesson 3: 

Step: Implement the key to colour mapping as a dictionary.

Step: Make the snake move by pressing the arrow keys
* set the snake's initial position to variables `snake_x` and `snake_y`

Step: Create a better geometry for the screen based on square size and number of squares.

Step: implement the snake a list of segments.  Each segment is a tuple of 2 values (x, y) representing the position of the segment.

"""
import pygame

# Set up constants for colours.
# Each colour is a tuple of red, green, blue  values.  Each value can range from 0 to 255.
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
    pygame.K_o: COLOUR_ORANGE,
}

# create a geometry based on square size and number of squares
SQUARE_SIZE = 20  # Size of each square in pixels
NUM_SQUARES_X = 32  # Number of squares horizontally
NUM_SQUARES_Y = 24  # Number of squares vertically
SCREEN_WIDTH = SQUARE_SIZE * NUM_SQUARES_X  # Total width of the screen
SCREEN_HEIGHT = SQUARE_SIZE * NUM_SQUARES_Y  # Total height of the screen

# set the initial position of the snake
snake_x = SCREEN_WIDTH / 2  # Initial x position of the snake
snake_y = SCREEN_HEIGHT /2  # Initial y position of the snake

snake = [ (snake_x, snake_y)
         , (snake_x-SQUARE_SIZE, snake_y)
         , (snake_x- 2 * SQUARE_SIZE, snake_y)]  # List to hold the snake's body segments

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
        # print(event)
        dx = 0
        dy = 0
        if event.type == pygame.KEYDOWN:
            # Check which key was pressed
            if event.key in KEY_COLOUR_MAP:
                colour = KEY_COLOUR_MAP[event.key]
            if event.key == pygame.K_UP:
                dy -= SQUARE_SIZE  # Move the snake up by 20 pixels
            elif event.key == pygame.K_DOWN:
                dy += SQUARE_SIZE  # Move the snake down by 20 pixels
            elif event.key == pygame.K_LEFT:
                dx -= SQUARE_SIZE  # Move the snake left by 20 pixels
            elif event.key == pygame.K_RIGHT:
                dx += SQUARE_SIZE
        
            if dx !=0 or dy != 0:
                snake_x += dx
                snake_y += dy
            new_snake_head = (snake_x, snake_y)

            snake.insert(0, new_snake_head)
            # Remove the last segment of the snake to keep its length constant
            snake.pop()
    # Fill the background with black
    screen.fill(COLOUR_BLACK)

    for segment in snake:
        # Draw each segment of the snake
        pygame.draw.rect(screen, colour, [segment[0], segment[1], SQUARE_SIZE, SQUARE_SIZE])

    pygame.display.update()

    # Limit the frame rate to 5 frames per second (FPS)
    clock.tick(5)

pygame.quit()
