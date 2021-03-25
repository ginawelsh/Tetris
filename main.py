import pygame
import random
from math import pi
import time

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

# basic colours
WHITE = (255, 255, 255)
BLACK  = (0, 0, 0)
RED = (255, 0, 0, 125)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
SILVER = (192,192,192)
LIGHT_ORANGE= (255, 229, 204)
LIGHT_GREEN = (153, 255, 204)


# white colour  
colour = (255,255,255)  
  
# light shade of the button  
colour_light = (170,170,170)  
  
# dark shade of the button  
colour_dark = (100,100,100)  



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
#Since we will be creating multiple shapes it makes sense to 
# create a piece class that can store some information about each shape.
   
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
# Since we will be dropping shapes down the screen at random we need to generate a random shape. 
# This will be done in the get_shape() function.    
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

def text_objects(text, font):
    textSurface = font.render(text, True, YELLOW)
    return textSurface, textSurface.get_rect()


def main(): # launch main game
    pass
    

def main_menu():

    # initialise game machine

    pygame.init()


    # Set the height and width of the screen
    size = (720, 720)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Tetris Game (CodaBunga version 1.0)")

    # Define the colors we will use in RGB format (need to declare after game is init?)

    # white colour  
    colour = (255,255,255)  
  
    # light shade of the button  
    colour_light = (170,170,170)  
  
    # dark shade of the button  
    colour_dark = (100,100,100)  

    # stores the width of the  
    # screen into a variable  
    width = screen.get_width()  
  
    # stores the height of the  
    # screen into a variable  
    height = screen.get_height()  

    # defining a font  
    small_text = pygame.font.SysFont('Arial',35)  
    large_text = pygame.font.SysFont('Arial', 70)
  
    # rendering a text written in  
    # this font  
    start_text = small_text.render('START', True, BLACK, GREEN)  
    quit_text = small_text.render('QUIT', True, BLACK, RED)
    title_screen = large_text.render("Welcome to Tetris!", True, BLACK, LIGHT_GREEN)

    title_screen_obj = title_screen.get_rect()
    title_screen_obj.center = ((width/2), 125)

    done = False
    clock = pygame.time.Clock()


    while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
        clock.tick(10)

        screen.fill(LIGHT_GREEN)

        screen.blit(title_screen, title_screen_obj)

     
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
    
        # stores the (x,y) coordinates into  
        # the variable as a tuple  
        mouse = pygame.mouse.get_pos()

        if 310+150 > mouse[0] > 310 and 250+75 > mouse[1] > 250:
            pygame.draw.rect(screen, YELLOW, (300, 250, 150, 75))
           
        else:
            pygame.draw.rect(screen, GREEN, (300, 250, 150, 75))
        

        # if mouse hovers over button, the border around text turns yellow

        if 310+150 > mouse[0] > 310 and 450+75 > mouse[1] > 450:
            pygame.draw.rect(screen, YELLOW,(300,450,150,75))
           
        else:
            pygame.draw.rect(screen, RED,(300,450,150,75))


        # render text on menu screen buttons ("START" and "QUIT")
        screen.blit(start_text, (320, 262, 75, 37.5)) #(310,250,75,37.5)) 
        screen.blit(quit_text, (330, 462, 75, 37.5))
             

        #if the mouse is clicked on the QUIT button the game is terminated 
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if 310+150 > event.pos[0] > 310 and 450+75 > event.pos[1] > 450:
                    pygame.quit()
                    sys.exit()
    

        # Go ahead and update the screen with what we've drawn. 
        # This MUST happen after all the other drawing commands.
        pygame.display.update()
       # pygame.display.flip()

 
# Be IDLE friendly
pygame.quit()


main_menu() # start game