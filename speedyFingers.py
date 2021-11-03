import pygame
import button
from pygame.locals import *
import sys
import time
  
#initiliaze pygame
pygame.init()

#glabl variables
width = 1000
height = 700
screen  = pygame.display.set_mode((width,height))
gameOn = True

background = pygame.image.load("intro.png")
background = pygame.transform.scale(background, (width, height))

intro = pygame.image.load("intro.png")
intro = pygame.transform.scale(intro, (width, height))

#button images
arrow_img = pygame.image.load("arrow.png").convert_alpha()
arrow_img = pygame.transform.scale(arrow_img, (290, 290))

#play_img = pygame.image.load("play.png").convert_alpha()
#play_img = pygame.image.load("play.png").convert_alpha()

#rules_img = pygame.image.load("rules.png").convert_alpha()
#rules_img = pygame.image.load("rules.png").convert_alpha()




#button class
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action


#create button instances
arrow_button = Button(700, 350, arrow_img)











while gameOn:
    #taking event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
        if arrow_button.draw():
            print("ONTO THE NExT PAGEEE") 

    screen.blit(background, (0,0))
    arrow_button.draw()
    pygame.display.update()

