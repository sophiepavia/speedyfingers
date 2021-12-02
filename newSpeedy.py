import pygame
import button
from pygame.locals import *
import sys
import time
import DBsetup as DB
import random
import sqlite3 as sql

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
    directionsButton = Button((535, 480), (377, 133), (98, 219, 200), "Directions")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif playButton.is_clicked(event):
                print("play button pressed")
                play(screen, w, h)

            elif statsButton.is_clicked(event):
                stats(screen)
                print("stats button pressed")
            elif directionsButton.is_clicked(event):
                directions(screen)
                print("directions button pressed")

        screen.blit(background, (0, 0))
        playButton.draw(screen)
        statsButton.draw(screen)
        directionsButton.draw(screen)
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

    file = open('sentences.txt').read()
    sentences = file.split('\n')
    word= random.choice(sentences)

    background = pygame.image.load('play.png')
    background = pygame.transform.scale(background, (w, h))

    screen.fill((0,0,0))
    screen.blit(background, (0,0))

    pygame.draw.rect(screen,(102,255,243), (50,300,900,100), 2)

    #display sentence to type
    font = pygame.font.Font(None, 24)
    text = font.render(word, 1,(240,240,240))
    text_rect = text.get_rect(center=(1000/2, 275))
    screen.blit(text, text_rect)
    #directions
    font = pygame.font.Font(None, 20)
    text = font.render("Click box to type", 1,(240,240,240))
    text_rect = text.get_rect(center=(500, 415))
    screen.blit(text, text_rect)

    #back button
    backButton = Button((50, 600), (200, 90), (240,240,240), "Back to Main")
    backButton.draw(screen)

    running=True
    while running:
        #start time clock
        clock = pygame.time.Clock()

        #draw rect box
        screen.fill((240,240,240), (50,300,900,100))
        pygame.draw.rect(screen,(102,255,243), (50,300,900,100), 2)
        #updates typing string
        font = pygame.font.Font(None, 24)
        text = font.render(user_input, 1,(105,105,105))
        text_rect = text.get_rect(center=(1000/2, 350))
        screen.blit(text, text_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                x,y = pygame.mouse.get_pos()
                #set position for type rectangle box
                if(x>=50 and x<=900 and y>=200 and y<=750):
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

                    file = open('sentences.txt').read()
                    sentences = file.split('\n')
                    word= random.choice(sentences)

                    background = pygame.image.load('play.png')
                    background = pygame.transform.scale(background, (w, h))

                    screen.fill((240,240,240))
                    screen.blit(background, (0,0))

                    pygame.draw.rect(screen,(102,255,243), (50,300,900,100), 2)
                    #draw button again 
                    backButton.draw(screen)
                    #display new word
                    font = pygame.font.Font(None, 24)
                    text = font.render(word, 1,(240,240,240))
                    text_rect = text.get_rect(center=(1000/2, 275))
                    screen.blit(text, text_rect)

                    #directions
                    font = pygame.font.Font(None, 21)
                    text = font.render("Click box to type", 1,(240,240,240))
                    text_rect = text.get_rect(center=(500, 415))
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
                            #enter stats in db
                            with sql.connect("speedyfingersDB.db") as con:
                                cur = con.cursor()
                                #query for Stats
                                cur.execute("INSERT INTO Stats (totalTime,wpm,percent) VALUES (?,?,?)", (totalTime,wpm,percent) )
                                con.commit()
                            con.close()

                            #show reset button
                            results = "Time: " + str(round(totalTime)) + " secs   Percent: " + str(round(percent)) + "%" + "   WPM: " + str(round(wpm))
                            again = pygame.image.load('playagain.png')
                            again = pygame.transform.scale(again, (150,150))
                            screen.blit(again, (500-75, 750-250))

                        print(results)

                        font = pygame.font.Font(None, 28)
                        text = font.render(results, 1,(240, 240, 240))
                        text_rect = text.get_rect(center=(500, 450))
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
            elif backButton.is_clicked(event):
                mainMenu(screen, 1000, 750)
        #screen.blit(background, (0, 0))
    clock.tick(60)




def directions(screen):
    background = pygame.image.load('directions.png')
    background = pygame.transform.scale(background, (1000, 750))

    screen.fill((0,0,0))
    screen.blit(background, (0,0))

    backButton = Button((150, 600), (200, 90), (240, 240, 240), "Back to Main")

    directions = "Welcome to the best game ever: SpeedyFingers!!" 
    #To play the game, type the sentence shown as fast and as accurate as you can"
    font = pygame.font.Font(None, 45)
    text = font.render(directions, 1,(105,105,105))
    text_rect = text.get_rect(center=(1000/2, 200))
    screen.blit(text, text_rect)

    font1 = pygame.font.Font(None, 30)
    directions1 = "To play just click on the text box and type away"
    text1 = font1.render(directions1, 1,(105,105,105))
    text_rect1 = text.get_rect(center=(600, 300))
    screen.blit(text1, text_rect1)

    directions2 = "Follow the sentence to a T to get the best score"
    text2 = font1.render(directions2, 1,(105,105,105))
    text_rect2 = text.get_rect(center=(600, 350))
    screen.blit(text2, text_rect2)

    directions3 = "Try your best and have fun! :)"
    text3 = font1.render(directions3, 1,(105,105,105))
    text_rect3 = text.get_rect(center=(600, 400))
    screen.blit(text3, text_rect3)

    #screen.blit(background, (0, 0))
    backButton.draw(screen)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif backButton.is_clicked(event):
                print("back button pressed")
                mainMenu(screen, 1000, 750)

        #screen.blit(background, (0, 0))
        #backButton.draw(screen)
        #pygame.display.update()

def stats(screen):
    #connect to db
    con = sql.connect("speedyfingersDB.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    #query executed
    cur.execute('select * from Stats ORDER BY percent DESC LIMIT 5')
    #get results
    rows = cur.fetchall()

    i = 0
    results = []
    for _ in rows:
        i +=1
        arr = [_ for y in rows for y in _]
        time = round(arr[i][0])
        wpm = round(arr[i][1])
        percent = round(arr[i][2])
        final = str(time) + "          " + str(wpm) + "            "+ str(percent)
        results.append(final)

    background = pygame.image.load('stats.png')
    background = pygame.transform.scale(background, (1000, 750))

    screen.fill((0,0,0))
    screen.blit(background, (0,0))

    backButton = Button((75, 600), (200, 90), (98, 219, 200), "Back to Main")

    directions = "All Time Top 5! (Ranked by best Percent!)" 
    font = pygame.font.Font(None, 45)
    text = font.render(directions, 1,(105,105,105))
    text_rect = text.get_rect(center=(1000/2, 300))
    screen.blit(text, text_rect)


    stats = "Time  WPM  Percent"
    font = pygame.font.Font(None, 45)
    text = font.render(stats, 1,(105,105,105))
    text_rect = text.get_rect(center=(1000/2, 340))
    screen.blit(text, text_rect)

    row = 400
    font1 = pygame.font.Font(None, 30)
    for res in results:
        text1 = font1.render(res, 1,(105,105,105))
        screen.blit(text1, (395, row))
        row += 50

    backButton.draw(screen)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif backButton.is_clicked(event):
                print("back button pressed")
                mainMenu(screen, 1000, 750)



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
