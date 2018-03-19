import numpy as np

# Import a library of functions called 'pygame'
import pygame

from STRING import *


def req_main_map():
    """
    return main_map of game

    # --- map RULE
    # 0 = empty
    # 1 = wall
    # 2 = food
    # 3 = snake head
    # 4 = snake body

    :return:
     main_map array in numpy format
     -1 if game finished
    """
    # TODO: write this func
    pass


def move_snake(direction):
    """
    get direction and move the head of snake
    and report problem
    :param direction:
    'up' for up
    'down' for down
    'left' for left
    'right' for right
    :return:
    'ok' => if no problem to move snake
    'dead-wall' => if snake crash into wall
    'dead-body' => if snake crash into the body
    'dead-win' => if map is full
    'dead' => snake died, but i can't( or don't want to) figure out
    """
    # TODO: write this func
    pass


def _update_movement():
    # update movement of user into map and return result
    # TODO: write this func
    pass


def _show_map(new_map, screen_obj):
    """
    draw map
    :param new_map:
     main_map in numpy format
    :return:
    """
    # TODO: this is working but this dude is too slow, fix this with metode blow
    # you just need to re draw pixels changes

    i_i = 0
    for i in new_map:
        j_j = 0
        for j in i:

            color_of_rect = 0
            if j == 0:
                # set color_of_rect to black for blank space
                color_of_rect = BLACK
            elif j == 1:
                # set color_of_rect to white for wall
                color_of_rect = GRAY
            elif j == 2:
                # set color_of_rect to red for food
                color_of_rect = RED
            elif j == 3:
                # set color_of_rect to blue for head of snake head
                color_of_rect = BLUE
            elif j == 4:
                # set color_of_rect to light_blue for snake body
                color_of_rect = LIGHT_BLUE

            # Draw a rectangle in i_i,j_j

            pygame.draw.rect(screen_obj, color_of_rect,
                             [(i_i * 15), (j_j * 15), 13, 13], 0)

            j_j += 1

        i_i += 1


# --- map RULE
# 0 = empty
# 1 = wall
# 2 = food
# 3 = snake head
# 4 = snake body

# set map size(-2 for walls)
_MAP_SIZE = 32
# create a main map for snake
main_map = np.zeros((_MAP_SIZE, _MAP_SIZE))
# create map wall
main_map[0, 0:] = 1
main_map[0:, 0] = 1
main_map[_MAP_SIZE - 1, 0:] = 1
main_map[0:, _MAP_SIZE - 1] = 1

# game status flag.
# if == True => game still playable
# if == False => game is finished and snake dead
_game_status_flag = True

# Initialize the game engine
pygame.init()

# Set the height and width of the screen
size = (800, 550)
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
    _show_map(main_map, screen)
    # ------- FIN DRAW CODE

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# close and showdown game engine
pygame.quit()
