import pygame
import random
from math import pi

# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

# GLOBAL VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height


# SHAPE FORMATS

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
# shape_colors = [white, black, red, blue, green, yellow, orange]
# index 0 - 6 represent shape



class Piece(object):
#Since we will be creating multiple shapes it makes sense to create a piece class that can store some information about each shape.
    pass

def create_grid(locked_positions={}):
# The way that we will keep track of pieces in the game is using a grid data structure. We will create a multidimensional list that contains 20 lists of 10 
# elements (rows and columns). Each element in the lists will be a tuple representing the color of the piece in that current position. This will allow us to draw all 
# of the colored squares quite easily as we can simply loop through the multidimensional list.
# The locked position parameter will contain a dictionary of key value pairs where each key is a position of a piece that has already fallen and each value is its color. 
# We will loop through these locked positions and modify our blank grid to show these pieces.
      pass

def convert_shape_format(shape):
    pass

def valid_space(shape, grid):
    pass

def check_lost(positions):
    pass

def get_shape():
# Since we will be dropping shapes down the screen at random we need to generate a random shape. This will be done in the get_shape() function.    
    pass

def draw_text_middle(text, size, color, surface):  
    pass
   
def draw_grid(surface, row, col):
    pass

def clear_rows(grid, locked):
    pass

def draw_next_shape(shape, surface):
    pass

def draw_window(surface):
    pygame.draw.rect #(surface, (255, 255, 255))

def main(): #this is where the game goes?
    pass
    

def main_menu():
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0, 125)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    orange = (255, 128, 0)

    # initialise game machine

    pygame.init()

    # Set the height and width of the screen
    size = [600, 450]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Tetris Game (CodaBunga version 1.0)")

    # Define the colors we will use in RGB format (need to declare after game is init?)

    WHITE = (255, 255, 255)
    BLACK  = (0, 0, 0)
    RED = (255, 0, 0, 125)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0, 0)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 128, 0)



    done = False
    clock = pygame.time.Clock()

    while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
        clock.tick(10)
     
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.


   # Clear the screen and set the screen background
        screen.fill(GREEN)

    # draw rectangle for main menu
        button = pygame.draw.rect(screen, YELLOW, [150, 10, 50, 20])

        pygame.Rect.inflate(button)
     


    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
        pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()


    

main_menu() # start game