import numpy as np
import random
# Import a library of functions called 'Pygame'
import pygame

from STRING import *


class SnakeGame:
    def __init__(self, map_size):

        # create a main map for snake
        self._main_map = self._create_map(map_size)

        self._screen = None
        self._screen_size = None

        # game status flag.
        # if == 1 => game still playable
        # if == 0 => game is finished and snake dead
        # if == -1 => game not began yet
        self._game_status_flag = -1

        # Initialize the game engine
        pygame.init()
        pass

    def __del__(self):
        # close and showdown game engine
        pygame.quit()

        pass

    def req_main_map(self):
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
        # cheack game not finished yet

        return self._main_map

    def move_snake(self, direction):
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

    def start_game(self, screen_size=(800, 550), game_fps=20, game_name="Snake AI"):
        """

        :param screen_size:
         size of screen in pixel
        :param game_fps:
        fps of this game
        :param game_name:
         name show in top of window
        :return:
        """
        # Change game status
        self._game_status_flag = 1

        # Set the height and width of the screen
        self._screen_size = screen_size

        # create a obj for screen
        self._screen = pygame.display.set_mode(self._screen_size)

        # set caption fow window
        pygame.display.set_caption(game_name)

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
            self._screen.fill(WHITE)

            # ------- DRAW CODE
            self._show_map()
            # ------- FIN DRAW CODE

            # Go ahead and update the screen with what we've drawn.
            # This MUST happen after all the other drawing commands.
            pygame.display.flip()

            # This limits the while loop to a max of 60 times per second.
            # Leave this out and we will use all CPU we can.
            clock.tick(game_fps)

        pass

    def _update_movement(self, ):
        # update movement of user into map and return result
        # TODO: write this func
        pass

    # Done
    def _show_map(self):
        """
        draw map
        :return:
        """
        # TODO: this is working but this dude is too slow, fix this with metode blow
        # you just need to re draw pixels changes

        i_i = 0
        for i in self._main_map:
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

                pygame.draw.rect(self._screen, color_of_rect,
                                 [(i_i * 15), (j_j * 15), 13, 13], 0)

                j_j += 1

            i_i += 1

    def _create_snake(self, size=5):
        """
        create a random snake in the main_map

        :param size:
        length of snake
        min 2
        max 20
        :return:
        0 => snake added
        'NoSpace' => not enough space for create snake
        'inValLen' => invalid length of snake
        """
        black_houses = self.__black_house_list(self._main_map)
        # check for space for create snake
        if len(black_houses) <= size:
            # NO space for create snake
            return 'NoSpace'

        # check len of snake
        if size < 2 or size > 20:
            return 'inValLen'

        # choose a random dot in empty space of array

        # add tail

        pass

    # Done
    @staticmethod
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
    def _add_food(self,  n=1):
        """
        add n food in empty space of map

        :param n:
         number of food
         default = 1
        :return:
        0 if no problem
        1 if no space for add any more food
        """
        black_house = self.__black_house_list(self._main_map)

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
            self._main_map[temp[0], temp[1]] = 2

        return 0

    # Done
    @staticmethod
    def _create_map(map_size=15):
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
