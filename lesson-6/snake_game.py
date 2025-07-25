""" Lesson 6: 
Objective
*********
Create food as a single red square randomly placed on the board

When the head of the snake collides with the food
- the snake will eat the food and grow by one segment
- the food will be removed from the board and another piece of food will be placed randomly on the board

Notes
*****
A short sound file of a snake eating food is in the resources folder

Steps
*****
These are the steps to complete the code in this lesson:

Import the random module

Create a Food class:
- with property position, a tuple of (x, y) coordinates
- a method set_random_position that generates a random position for the food within the board limits
- the __init__ method uses the set_random_position method to initialize the food's position
- a __str__ method to return a string representation of the food's position

Create an instance of the Food class at the start of the game

Create function draw_food: draw the food on the screen

Extend our Snake class so that the snake can eat some food and grow
- add a property length (and set to 3 initially)
- add a method increment_length
- change the move method so that it only pops the last segment if the length of the body is greater then the length property
- add a method eat() that plays the sound file and increments the snake's length property

Create function check_collision: check for collision between the snake's head and the food 
i.e. these are in the same position 
If  so, 
- the snake eats the food
- reposition the food randomly on the board
- increment the snake's length 
"""
import pygame
import random

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

EAT_SOUND_FILE = "resources/snake_eat.mp3"  # Path to the sound file for eating food

class Food:
    """A class to represent food in the game."""
    
    def __init__(self):
        """Initialize the food's position randomly within the board limits."""
        self.set_random_position()
        self.colour = COLOUR_RED  # Set the food's colour to red

    def set_random_position(self):
        """Set the food's position to a random square on the board."""
        x = random.randint(0, NUM_SQUARES_X - 1)
        y = random.randint(0, NUM_SQUARES_Y - 1)
        self.position = (x, y)

    def __str__(self):
        """Return a string representation of the food's position."""
        return f"Food(position={self.position} colour={self.colour})"


class Snake:
    """A class to represent the snake in the game."""
    
    def __init__(self, colour=COLOUR_GREEN):
        """Initialize the snake's body, colour, position, and direction."""
        self.colour = colour
        self.dx = 1  # Change in x (horizontal movement)
        self.dy = 0  # Change in y (vertical movement)
        self.length = 3  # Initial length of the snake
        
        initial_position = (NUM_SQUARES_X // 2, NUM_SQUARES_Y // 2)  # Start in the middle of the board
        
        self.body = []
        for i in range(self.length):
            self.body.append((initial_position[0] - i, initial_position[1]))  # Add segments to the left of the head

    def __str__(self):
        """Return a string representation of the snake's body and position."""
        return f"Snake(body={self.body}, colour={self.colour}, dx={self.dx}, dy={self.dy})"

    def move(self):
        """Update the snake's position and body segments based on the current direction."""
        old_head_x, old_head_y = self.body[0]
        new_head = (old_head_x + self.dx, old_head_y + self.dy)
        self.body.insert(0, new_head)  # Add new head at the front
        if len(self.body) > self.length:
            self.body.pop()  # Remove the last segment

    def is_out_of_bounds(self):
        """Check if the snake's head is out of bounds of the screen."""
        x_pos, y_pos = self.body[0]
        return (x_pos < 0 or x_pos >= NUM_SQUARES_X or 
                y_pos < 0 or y_pos >= NUM_SQUARES_Y)
                
    def increment_length(self):
        """Increase the length of the snake by one segment."""
        self.length += 1
        print(f"Snake length increased to {self.length}")

    def eat(self):
        """Play the eating sound and increment the snake's length."""
        pygame.mixer.music.load(EAT_SOUND_FILE)
        pygame.mixer.music.play(0)
        self.increment_length()

        
# Functions

def draw_snake(SQUARE_SIZE, snake,  screen):
    """Draw the snake on the screen as a series of rectangles."""
    for segment in snake.body:
        pygame.draw.rect(screen, snake.colour, [segment[0]*SQUARE_SIZE, segment[1]*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE])

def draw_food(SQUARE_SIZE, food, screen):
    """Draw the food on the screen as a red square."""
    pygame.draw.rect(screen, food.colour, [food.position[0]*SQUARE_SIZE, food.position[1]*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE])

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

def check_collision(snake, food):
    """Check if the snake's head collides with the food."""
    if snake.body[0] == food.position:
        return True
    return False

# Initialise the snake, food and set up game variables

snake = Snake()  # Create an instance of the Snake class
food = Food()  # Create an instance of the Food class
print(f"food created at {food}")

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
                snake.colour = KEY_COLOUR_MAP[event.key]
                print(f"Colour changed to {snake.colour}")

            # Set dx and dy values based on the arrow keys pressed
            snake.dx, snake.dy = change_snake_direction(snake.dx, snake.dy, event)
            
    # Update the snake's position based on the current direction
    snake.move()

    if check_collision(snake, food):
        print("Snake has eaten the food!")
        snake.eat()
        food.set_random_position()

    # Check if the snake is out of bounds
    if snake.is_out_of_bounds():
        print("Game Over! The snake has gone out of bounds.")
        game_over = True
        continue

    # Fill the background with black
    screen.fill(COLOUR_BLACK)

    # Draw the snake as a set of rectangles for each segment
    draw_snake(SQUARE_SIZE, snake, screen)
    draw_food(SQUARE_SIZE, food, screen)

    pygame.display.update()  
    clock.tick(FRAME_RATE)

pygame.quit()
