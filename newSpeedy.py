import pygame
import button
from pygame.locals import *
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

    background = pygame.image.load('menu.png')

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
                play(screen, w, h)

            elif statsButton.is_clicked(event):
                print("stats button pressed")
            elif otherButton.is_clicked(event):
                print("other button pressed")

        screen.blit(background, (0, 0))
        playButton.draw(screen)
        statsButton.draw(screen)
        otherButton.draw(screen)
        pygame.display.update()

def play(screen, w,h):


    user_input = ''
    word = ''

    start = 0
    totalTime = 0
    wpm = 0

    isActive = False
    reset = False
    end = False

    word = 'Hello my name is'

    background = pygame.image.load('play.png')
    background = pygame.transform.scale(background, (w, h))

    screen.fill((0,0,0))
    screen.blit(background, (0,0))

    pygame.draw.rect(screen,(102,255,243), (250,300,500,100), 2)

    font = pygame.font.Font(None, 28)
    text = font.render(word, 1,(240,240,240))
    text_rect = text.get_rect(center=(1000/2, 200))
    screen.blit(text, text_rect)
    #pygame.display.update()

    running=True
    while running:
        #start time clock
        clock = pygame.time.Clock()

        #draw rect box
        screen.fill((240,240,240), (250,300,500,100))
        pygame.draw.rect(screen,(102,255,243), (250,300,500,100), 2)
        #updates typing string
        font = pygame.font.Font(None, 28)
        text = font.render(user_input, 1,(0,0,0))
        text_rect = text.get_rect(center=(1000/2, 375))
        screen.blit(text, text_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                x,y = pygame.mouse.get_pos()
                #set position for type rectangle box
                if(x>=250 and x<=500 and y>=300 and y<=750):
                    isActive = True
                    input_text = ''
                    start = time.time()
                # position of reset box
                if(x>=310 and x<=510 and y>=390 and end):
                    user_input = ''
                    word = ''

                    start = 0
                    totalTime = 0
                    wpm = 0

                    isActive = False
                    reset = False
                    end = False

                    word = 'Hello my name is'

                    background = pygame.image.load('play.png')
                    background = pygame.transform.scale(background, (w, h))

                    screen.fill((240,240,240))
                    screen.blit(background, (0,0))

                    pygame.draw.rect(screen,(102,255,243), (250,300,500,100), 2)

                    font = pygame.font.Font(None, 28)
                    text = font.render(word, 1,(240,240,240))
                    text_rect = text.get_rect(center=(1000/2, 200))
                    screen.blit(text, text_rect)
                    pygame.display.update()
                    x,y = pygame.mouse.get_pos()

            elif event.type == pygame.KEYDOWN:
                if isActive and not end:
                    if event.key == pygame.K_RETURN:
                        print(user_input)
                        #get results and stats of play
                        if not end:
                            totalTime = time.time() - start

                            count = 0
                            for i, char in enumerate(word):
                                try:
                                    if user_input[i] == char:
                                        count +=1
                                except:
                                    pass
                            percent = count/len(word)*100

                            wpm = len(user_input)*60/(5*totalTime)
                            end = True
                            #show reset button
                            results = "Time: " + str(round(totalTime)) + "secs Percent: " + str(round(percent)) + "%" + "   WPM: " + str(round(wpm))
                            again = pygame.image.load('playagain.png')
                            again = pygame.transform.scale(again, (150,150))
                            screen.blit(again, (500-75, 750-140))

                        print(results)

                        font = pygame.font.Font(None, 28)
                        text = font.render(results, 1,(240, 240, 240))
                        text_rect = text.get_rect(center=(500, 600))
                        screen.blit(text, text_rect)

                        end = True
                        pygame.display.update()


                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    else:
                        try:
                           user_input += event.unicode
                        except:
                           pass

        #screen.blit(background, (0, 0))
    clock.tick(60)


def draw_text(screen, msg, y ,fsize, color):
    font = pygame.font.Font(None, fsize)
    text = font.render(msg, 1,color)
    text_rect = text.get_rect(center=(1000/2, y))
    screen.blit(text, text_rect)
    pygame.display.update()


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
