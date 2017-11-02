"""
this is the main game file , this is the core of the game
"""
import math
import random
import pygame


#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# This class is for the ball
#it uses the sprite class in pygame
class TheBall(pygame.sprite.Sprite):

	#Constructor. Input color of block and x and y position

    def __init__(self):
		#call the sprite constructor
        super().__init__()
		#create the image of the ball
        self.image = pygame.Surface([10, 10])
		#make the ball white
        self.image.fill(WHITE)
		#get the rectangle that shows the image's location
        self.rect = self.imgage.get_rect()
		#define variables for our width and height of our screen
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
		#the speed for the pixels
        self.speed = 0

		#points representing where the ball is
        self.x = 0
        self.y = 0
        #direction in degrees
        self.direction = 0
        #height and width of the ball-
        self.width = 10
        self.height = 10
        #initalize ball speed and position
        self.reset()

    def reset(self):
        self.x = random.randrange(50, 750)
        self.y = 350.0
        self.speed = 8.0
        #direction of ball 
        self.direction = random.randrange(-45, 45)
        #flip a coin
        if random.randrange(2) == 0:
            #reverse the ball direction let opponent get it first
            self.direction += 180
            self.y = 50
    
    #bounce the ball off a horizontal surface
    def bounce(self, diff):
        self.direction = (180 - self.direction) % 360
        self.direction -= diff
        #speed it up
        self.speed *= 1.1

    #update position of the ball
    def update(self):
        #sine and cosine conversion
        direction_radians = math.radians(self.direction)
        #change position based on speed and direction
        self.x += self.speed * math.sin(direction_radians)
        self.y -= self.speed * math.cos(direction_radians)

        if self.y < 0:
            self.reset()
        if self.y > 600:
            self.reset()
            #move image to positions
        self.rect.x = self.x
        self.rect.y = self.y

        #Do we bounce off the left side of the screen
        if self.x <= 0:
            self.direction = (360-self.direction) % 360
            print (self.direction)
        #do we bounce off the right side?
        if self.x > self.screenwidth - self.width:
            self.direction = (360 - self.direction) % 360
    #this class represents the player
class ThePlayer(pygame.sprite.Sprite):
    #constructor
    def __init__(self, joystick, y_pos):
        #call sprite constructor
        super().__init__()
        self.width = 75
        self.height = 15
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
        self.joystick = joystick
        #make the top left corner the location to pass to
        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()

        self.rect.x = 0
        self.rect.y = y_pos

    #update player
    def update(self):
        #get position of the axis on the game controller
        #returns a number between -1.0 and 1.0
        horizontal_axis_position = self.joystick.get_axis(0)

        #move x according to the axis , multiply it by 15 to make it faster.
        self.rectangle.x = int(self.rectangle.x + horizontal_axis_position)
     #make sure paddle isnt off the screen
        if self.rectangle.x > self.screenwidth - self.width:
            self.rectangle.x = self.screenwidth - self.width

SCORE1 = 0
SCORE2 = 0
#initalize pygame
pygame.init()
#create a 800 x 600 window
window = pygame.display.set_mode([800, 600])

#title of the window
pygame.display.set_caption('Pong')

#make mouse disappear when mouse is over window

pygame.mouse.set_visible(0)
#font to draw text
font = pygame.font.Font(None, 36)
#make surface we can draw on
background = pygame.Surface(screen.get_size())
ball = TheBall()
#make a group of 1 ball so we can check collisions
balls = pygame.sprite.Group()
balls.add(ball)

joystick_count = pygame.joystick.get_count()
if joystick_count < 1:
    #no joystick
    print ('Error no joystick detected')
    pygame.quit()
    exit()
else:
    #use joystick 0 and initalize
    joystick1 = pygame.joystick.Joystick(0)
    joystick1.init()
    joystick2 = pygame.joystick.Joystick(1)
    joystick2.init()
player1 = ThePlayer


