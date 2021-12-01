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
        otherButton.draw(screen)
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
