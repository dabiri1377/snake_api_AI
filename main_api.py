import numpy as np

# Import a library of functions called 'pygame'
import pygame

from STRING import *


def req_main_map():
    # send main map array
    # TODO: write this func
    pass


def move_snake():
    # TODO: write brief help
    # TODO: write this func
    pass


# --- map RULE
# 0 = empty
# 1 = wall
# 2 = food
# 8 = snake head
# 3 = snake body

# set map size(-2 for walls)
MAP_SIZE = 32
# create a main map for snake
main_map = np.zeros((MAP_SIZE, MAP_SIZE))
# create map wall
main_map[0, 0:] = 1
main_map[0:, 0] = 1
main_map[MAP_SIZE-1, 0:] = 1
main_map[0:, MAP_SIZE-1] = 1

# for_debug
print(main_map)



# Initialize the game engine
pygame.init()

# Set the height and width of the screen
size = (500, 500)
screen = pygame.display.set_mode(size)

# set caption fow window
pygame.display.set_caption("Snake AI")

# var for Loop until the user clicks the close button.
done = False

# define obj for frame rate
clock = pygame.time.Clock()

# Loop as long as done == False
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # --- Game logic should go here

    # All drawing code happens after the for loop and but
    # inside the main while not done loop.

    # Clear the screen and set the screen background
    screen.fill(WHITE)

    # ------- DRAW CODE

    # ------- FIN DRAW CODE

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# close and showdown game engine
pygame.quit()
