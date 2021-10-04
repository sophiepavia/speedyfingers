import pygame
from pygame.locals import *
import sys
import time
import random
# 750 x 500    

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

        self.stage_1 = pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption('Speedy Fingers')

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
            self.stage_1.fill((0,0,0), (50,250,650,50))
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    sys.exit()

    def reset_now(self):
        #go to intro screen, maybe in future change to go home screen?
        self.stage_1.blit(self.show_intro, (0,0))
        pygame.display.update()

        #wait 5 seconds on intro screen
        time.sleep(3)

        self.reset=False
        self.end = False


        #draw home screen
        self.stage_1.fill((0,0,0))
        self.stage_1.blit(self.home,(0,0))
        #home message on main stage filled with background
        msg = "Speedy"
        msg2 = "Fingers"
        self.draw_text(self.stage_1, msg,300, 80,self.HEAD_C)  
        self.draw_text(self.stage_1, msg2,400, 80,self.HEAD_C) 
        pygame.display.update()

        
Game().run()
