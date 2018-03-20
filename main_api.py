import numpy as np
import random
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


# Done
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


def _create_snake(new_map, size=5):
    """
    create a random snake in the main_map
    :param new_map:
     main_map
    :param size:
    length of snake
    min 2
    max 20
    :return:
    0 if can add snake
    """
    black_houses = __black_house_list(new_map)
    # choose a random dot in empty space of array

    # add tail

    pass


# Done
def __black_house_list(new_map):
    """
    return list of black house's
    :param new_map:
     main_map
    :return:
     list of black house in normal array
    """
    addr_black = []  # list of black house
    i_i = 0
    # find all black house
    for i in new_map:
        j_j = 0
        for j in i:
            if j == 0:
                addr_black.append([i_i, j_j])
            j_j += 1
        i_i += 1
    return addr_black


# Done
def _add_food(new_map, n=1):
    """
    add n food in empty space of map
    :param new_map:
     main_map
    :param n:
     number of food
     default = 1
    :return:
    0 if no problem
    1 if no space for add any more food
    """
    black_house = __black_house_list(new_map)

    if len(black_house) == 0:
        return 1

    # pick n ta random house and put it into rand_list
    rand_list = []
    for k in range(n):
        rand_dot = random.randint(0, len(black_house))
        temp = black_house[rand_dot]
        rand_list.append(temp)
        del black_house[rand_dot]

    for k in range(n):
        temp = rand_list.pop()
        new_map[temp[0], temp[1]] = 2

    return 0


# Done
def create_map(map_size=15):
    """
    create a (map_size x map_size) map
    set wall and return it

    # --- map RULE
    # 0 = empty
    # 1 = wall
    # 2 = food
    # 3 = snake head
    # 4 = snake body

    :param map_size:
    size of map(n x n)
    :return:
     matrix of map in numpy form
    """

    # create a main map for snake
    temp_main_map = np.zeros((map_size, map_size))
    # create map wall
    temp_main_map[0, 0:] = 1
    temp_main_map[0:, 0] = 1
    temp_main_map[map_size - 1, 0:] = 1
    temp_main_map[0:, map_size - 1] = 1

    return temp_main_map


# create a main map for snake
main_map = create_map(10)

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
    clock.tick(1)

# close and showdown game engine
pygame.quit()
