# Import a library of functions called 'pygame'
import pygame

from STRING import *

# Initialize the game engine
pygame.init()


# Set the height and width of the screen
size = (500, 500)
screen = pygame.display.set_mode(size)

# set caption fow window
pygame.display.set_caption("Professor Craven's Cool Game")

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
