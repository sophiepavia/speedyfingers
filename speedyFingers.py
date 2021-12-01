import pygame
import button
from pygame.locals import *
import sys
import time



stage_1 = pygame.display.set_mode((1000,750))

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
            stage_1.blit(self.image, (self.rect.x, self.rect.y))

        return action

class Game:

    def __init__(self):
        self.w=1000
        self.h=750
        self.reset=True
        self.active = False
        self.end = False
        self.HEAD_C = (255,213,102)
        self.TEXT_C = (300,300,300)

        pygame.init()

        self.show_intro = pygame.image.load('intro.png')

        self.show_intro = pygame.transform.scale(self.show_intro, (self.w,self.h))


        self.home = pygame.image.load('home.png')
        self.home = pygame.transform.scale(self.home, (self.w,self.h))

        #stage_1 = pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption('Speedy Fingers')

        #button images
        self.arrow_img = pygame.image.load("arrow.png").convert_alpha()
        self.arrow_img = pygame.transform.scale(self.arrow_img, (290, 290))

        #from tutorial
    def draw_text(self, screen, msg, y ,fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1,(0,128,128))
        text_rect = text.get_rect(center=(self.w/3.5, y))
        screen.blit(text, text_rect)
        pygame.display.update()


    def run(self):
    #reset from top
        self.reset_now()
        #set status to true
        self.running=True

        #if game is running, look for events
        while(self.running):
            stage_1.fill((0,0,0), (50,250,650,50))
            arrow_button = Button(700, 350, self.arrow_img)
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    sys.exit()

                if arrow_button.draw() == True:
                    #draw home screen
                    stage_1.fill((0,0,0))
                    stage_1.blit(self.home,(0,0))
                    #home message on main stage filled with background
                    msg = "Speedy"
                    msg2 = "Fingers"
                    self.draw_text(stage_1, msg,300, 80,self.HEAD_C)
                    self.draw_text(stage_1, msg2,400, 80,self.HEAD_C)
                    pygame.display.update()

    def reset_now(self):
    #go to intro screen, maybe in future change to go home screen
        stage_1.blit(self.show_intro, (0,0))
        pygame.display.update()

        self.reset=False
        self.end = False

Game().run()

