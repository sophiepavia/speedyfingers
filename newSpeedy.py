import pygame
import button
from pygame.locals import *
import pygame.freetype
import sys
import time
import DBsetup as DB



def main():
    pygame.init()
    DB.createDB()
    width = 1000
    height = 750

    # show intro screen
    screen = pygame.display.set_mode((width, height))
    introScreen(screen, width, height)


def introScreen(screen, w, h):
    background = pygame.image.load('intro.png')
    background = pygame.transform.scale(background, (w, h))
    pygame.display.set_caption("SpeedyFingers")
    nextScreenButton = Button((360, 560), (345, 100), (98,219,200), "Go to Main Menu")
    white = (255, 255, 255)
    while True:
        # screen.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if nextScreenButton.is_clicked(event):
                print("button pressed")
                mainMenu(screen, w, h)
        screen.blit(background, (0, 0))
        nextScreenButton.draw(screen)
        pygame.display.update()

def mainMenu(screen, w, h):
    background = pygame.image.load('home.png')
    background = pygame.transform.scale(background, (w, h))
    pygame.display.set_caption("Main Menu")

    playButton = Button((535, 68), (377, 133), (98,219,200), "Play!")
    statsButton = Button((535, 270), (377, 133), (98, 219, 200), "Check Your Stats!")
    otherButton = Button((535, 480), (377, 133), (98, 219, 200), "What do you guys want to put here?")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif playButton.is_clicked(event):
                print("play button pressed")
            elif statsButton.is_clicked(event):
                print("stats button pressed")
            elif otherButton.is_clicked(event):
                print("other button pressed")

        screen.blit(background, (0, 0))
        playButton.draw(screen)
        statsButton.draw(screen)

# play mode screen
def play(screen, w,h):

    #function var for sentences
    user_input = ''
    word = ''
    #for timing 
    start = 0
    totalTime = 0
    #wpm stats 
    wpm = 0
    #game mode vars
    isActive = False
    reset = False
    end = False

    #pull random sentence from txt file
    file = open('sentences.txt').read()
    sentences = file.split('\n')
    word= random.choice(sentences)

    #set play background
    background = pygame.image.load('play.png')
    background = pygame.transform.scale(background, (w, h))

    #set & blit screen for background
    screen.fill((0,0,0))
    screen.blit(background, (0,0))

    #draw text box
    pygame.draw.rect(screen,(102,255,243), (50,300,900,100), 2)

    #display sentence to type
    VIEJO
    font = pygame.font.Font(None, 24)
    text = font.render(word, 1,(240,240,240))

    # #NUEVO
    currentIdx = 0
    # font = pygame.freetype.Font(None, 24)
    # font.origin = True
    # fHeight = font.get_sized_height()
    # # print("Freetype font height is: ", fHeight)
    # horAdvance = 4
    # text_rect = font.get_rect(word)
    # baseline = text_rect



    text_rect = text.get_rect(center=(1000/2, 275))
    screen.blit(text, text_rect)

    #display directionsa
    font = pygame.font.Font(None, 20)
    text = font.render("Click box to type", 1,(240,240,240))
    text_rect = text.get_rect(center=(500, 415))
    screen.blit(text, text_rect)

    #back button
    backButton = Button((50, 600), (200, 90), (240,240,240), "Back to Main")
    backButton.draw(screen)


    running=True #state of game
    while running:

        #start time clock
        clock = pygame.time.Clock()

        #draw rect box
        screen.fill((240,240,240), (50,300,900,100))
        pygame.draw.rect(screen,(102,255,243), (50,300,900,100), 2)

        #updates user's input string
        font = pygame.font.Font(None, 24)
        text = font.render(user_input, 1,(105,105,105))
        text_rect = text.get_rect(center=(1000/2, 350))
        screen.blit(text, text_rect)



class Button(object):
    def __init__(self, position, size, color, text):
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = pygame.Rect((0, 0), size)

        font = pygame.font.SysFont(None, 32)
        text = font.render(text, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = self.rect.center

        self.image.blit(text, text_rect)

        # set after centering text
        self.rect.topleft = position

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)


main()
