import numpy as np
import random

# Import a library of functions called 'Pygame'
import pygame

from V1.STRING import *


class SnakeGame:
    def __init__(self, map_size=20, s_size=5):
        """

        :param map_size:
         size of map in block's
        :param s_size:
         size of snake
        """
        # create a main map for snake
        self._main_map = self._create_map(map_size)
        "main map of game in numpy ndarray format"

        self._screen = None
        "obj of screen"

        self._screen_size = None
        "size of screen in pixel"

        self._game_status_flag = -1
        """if == 1 => game still playable, 
        if == 0 => game is finished and snake dead, 
        if == -1 => game not began yet    
        if == 2 you win!!
        """

        self._game_win_flag_2 = 0
        "if == True => you won the game"

        self._snake_head = None
        "position of head of snake"

        self._snake = []
        """"list of all snake body part, in order
        (snake[0] = head of snake) """

        self._snake_size = s_size
        "size of snake"

        self._snake_score = 0
        "length added to snake for eating food"

        self._map_size = map_size

        # Initialize the game engine
        pygame.init()

        # create a snake in the map
        self._create_snake(s_size)

        # add a food into map
        self._add_food(1)

        pass

    def __del__(self):
        # close and showdown game engine
        pygame.quit()

        pass

    # Done
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
         -2 if game finished
         -1 if game not began yet
         -3 if you win
        """
        if self._game_win_flag_2 == 1:
            return -3

        if self._game_status_flag == 1:
            return self._main_map
        elif self._game_status_flag == -1:
            return -1
        elif self._game_status_flag == 0:
            return -2

    @staticmethod
    def done():
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                return False

        return True

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
        'died' => game is already finished
        1 => some other thing is wrong
        """
        # game already finished
        if self._game_status_flag == 0:
            return 'died'

        self._snake_head = self._snake[0]
        snake_head_i = self._snake_head[0]
        snake_head_j = self._snake_head[1]

        if direction == 'up':
            next_block = [snake_head_i - 1, snake_head_j]
        elif direction == 'down':
            next_block = [snake_head_i + 1, snake_head_j]
        elif direction == 'left':
            next_block = [snake_head_i, snake_head_j - 1]
        elif direction == 'right':
            next_block = [snake_head_i, snake_head_j + 1]
        else:
            return 1

        if self._main_map[next_block[0], next_block[1]] == 1:
            # crash to wall
            self._game_status_flag = 0
            self._update_screen()
            return 'dead-wall'

        elif self._main_map[next_block[0], next_block[1]] == 2:
            # snake eat food
            self._snake.insert(0, next_block)
            self._put_snake_in_map()
            self._update_screen()
            self._snake_score += 1
            if len(self.__food_house_list()) == 0 \
                    and len(self.__black_house_list()) == 0:
                self._game_win_flag_2 = 1
                return 'dead-win'
            else:
                return 'ok'

        elif self._main_map[next_block[0], next_block[1]] == 0:
            # snake just move
            self._snake.insert(0, next_block)
            self._snake = self._snake[:-1]
            self._put_snake_in_map()
            self._update_screen()
            if len(self.__food_house_list()) == 0 \
                    and len(self.__black_house_list()) == 0:
                self._game_win_flag_2 = 1
                return 'dead-win'
            else:
                return 'ok'

        elif self._main_map[next_block[0], next_block[1]] == 4:
            # crash to itself
            self._game_status_flag = 0
            self._update_screen()
            return 'dead-body'
        elif self._main_map[next_block[0], next_block[1]] == 3:
            # crash into his head?!!
            print("WFT? How?")
            return 1
        else:
            print("WTF?!!")
            return 1

    def start_game(self, screen_size=(700, 490), game_name="Snake AI"):
        """

        :param screen_size:
         size of screen in pixel

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
        self._update_screen()

        pass

    def _update_screen(self):
        # update movement of user into map and return result

        # clear screen
        self._screen.fill(WHITE)

        # ------- DRAW CODE

        # show maze_map
        self._show_map()

        # show score
        self._show_score()

        # ------- FIN DRAW CODE

        # update the screen with what we've drawn.
        pygame.display.flip()

        pass

    def _show_score(self):
        pygame.draw.line(self._screen, BLACK, [490, 0], [490, 490], 3)

        font = pygame.font.SysFont('Calibri', 30, False, False)

        text_string = "Score =" + str(self._snake_score)
        text = font.render(text_string, True, BLACK)

        self._screen.blit(text, [500, 10])

        if self._game_win_flag_2 == 1:
            # you win
            text = font.render("You win!!!", True, GREEN)
            self._screen.blit(text, [500, 50])
        elif self._game_status_flag == 0:
            # you lose
            text = font.render("You lose!!!", True, RED)
            self._screen.blit(text, [500, 100])
            pass

        pass

    # Done
    def _show_map(self):
        """
        draw map
        :return:
        """
        # TODO: this is working but this dude is too slow, fix this with method blow
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
                                 [(j_j * 15), (i_i * 15), 13, 13], 0)

                j_j += 1

            i_i += 1

    # need to work on
    def _create_snake(self, size=5):
        """
        create a random snake in the main_map
        (this func not working well. but develop later)
        :param size:
        length of snake
        min 2
        max 20
        (now its just 5 )
        :return:
        0 => snake added
        'NoSpace' => not enough space for create snake
        'inValLen' => invalid length of snake
        """
        black_houses = self.__black_house_list()
        # check for space for create snake
        if len(black_houses) <= size:
            # NO space for create snake
            return 'NoSpace'

        # check len of snake
        if size < 2 or size > 20:
            return 'inValLen'

        # for now size is 5 and position  is fixed
        # TODO: fix later
        self._snake = [[1, 6], [1, 5], [1, 4], [1, 3]]

        # put new snake in map
        self._put_snake_in_map()
        return 0

    # TODO: add some fucking command for this
    # TODO: fix this
    def _put_snake_in_map(self):
        food_list = self.__food_house_list()

        # clear main map
        # create a main map for snake
        self._main_map = np.zeros((self._map_size, self._map_size))
        # create map wall
        self._main_map[0, 0:] = 1
        self._main_map[0:, 0] = 1
        self._main_map[self._map_size - 1, 0:] = 1
        self._main_map[0:, self._map_size - 1] = 1

        # put back food into map
        for x in range(0, len(food_list)):
            self._main_map[food_list[x][0], food_list[x][1]] = 2

        # put snake into map
        self._main_map[self._snake[0][0], self._snake[0][1]] = 3
        for x in range(1, len(self._snake)):
            self._main_map[self._snake[x][0], self._snake[x][1]] = 4

    def __black_house_list(self):
        """
        return list of black house's

        :return:
         list of black house in normal array
        """
        addr_black = []  # list of black house
        i_i = 0
        # find all black house
        for i in self._main_map:
            j_j = 0
            for j in i:
                if j == 0:
                    addr_black.append([i_i, j_j])
                j_j += 1
            i_i += 1
        return addr_black

    def __food_house_list(self):
        """
        return list of food house's

        :return:
         list of food house in normal array
        """
        addr_food = []  # list of black house
        i_i = 0
        # find all black house
        for i in self._main_map:
            j_j = 0
            for j in i:
                if j == 2:
                    addr_food.append([i_i, j_j])
                j_j += 1
            i_i += 1
        return addr_food

    # Done
    def _add_food(self, n=1):
        """
        add n food in empty space of map

        :param n:
         number of food
         default = 1
        :return:
        0 if no problem
        1 if no space for add any more food
        """
        black_house = self.__black_house_list()

        if len(black_house) == 0:
            return 1

        # pick n ta random house and put it into rand_list
        rand_list = []
        for k in range(n):
            rand_dot = random.randint(0, len(black_house)-1)
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
        min = 7
        max = 32
        :return:
         matrix of map in numpy form
        """
        if map_size > 32:
            raise ImportError()

        # create a main map for snake
        temp_main_map = np.zeros((map_size, map_size))
        # create map wall
        temp_main_map[0, 0:] = 1
        temp_main_map[0:, 0] = 1
        temp_main_map[map_size - 1, 0:] = 1
        temp_main_map[0:, map_size - 1] = 1

        return temp_main_map
