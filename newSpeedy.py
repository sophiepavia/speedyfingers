import pygame
import button
from pygame.locals import *
import sys
import time
import DBsetup as DB #for DBsetup.py
import random
import sqlite3 as sql

# main program
def main():
    pygame.init()
    
    #window name
    pygame.display.set_caption('SpeedyFingers')

    #creates speedyfingersDB.db with DBsetup.py
    DB.createDB()

    #sets pygame width & height
    width = 1000
    height = 750

    # set intro screen
    screen = pygame.display.set_mode((width, height))
    introScreen(screen, width, height)

# main intro screen
def introScreen(screen, w, h):
    #set background to intro image
    background = pygame.image.load('intro.png')
    background = pygame.transform.scale(background, (w, h))

    #create arrow to main menu button
    arrowImg = pygame.image.load("arrow.png").convert_alpha()
    arrowImg = pygame.transform.scale(arrowImg, (250, 250))
    arrowImg = pygame.transform.rotate(arrowImg, 10)
    arrowButton = ButtonImage(705, 560, arrowImg)

    # event listener loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #exit window button
                pygame.quit()
                quit()

            #if arrow is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if arrowButton.draw(screen):
                    print("arrow button pressed")
                    mainMenu(screen, w, h) #go to main menu

        # blit screen with background & draw button
        screen.blit(background, (0, 0))
        screen.blit(arrowImg,(700,475))

        pygame.display.update()

# main menu screen
def mainMenu(screen, w, h):

    #set background to main menu screen
    background = pygame.image.load('menu.png')
    background = pygame.transform.scale(background, (w, h))

    #create mode buttons
    playButton = Button((535, 68), (377, 133), (98,219,200), "Play!")
    statsButton = Button((535, 270), (377, 133), (98, 219, 200), "Check Your Stats!")
    directionsButton = Button((535, 480), (377, 133), (98, 219, 200), "Directions")

    #action listener loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif playButton.is_clicked(event):
                print("play button pressed")
                play(screen, w, h) #go to play screen

            elif statsButton.is_clicked(event):
                stats(screen) #go to stats screen
                print("stats button pressed")

            elif directionsButton.is_clicked(event):
                directions(screen) #go to directions screen
                print("directions button pressed")

        #blit screen with background & buttons
        screen.blit(background, (0, 0))
        playButton.draw(screen)
        statsButton.draw(screen)
        directionsButton.draw(screen)
        pygame.display.update()

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
    font = pygame.font.Font(None, 24)
    text = font.render(word, 1,(240,240,240))
    text_rect = text.get_rect(center=(1000/2, 275))
    screen.blit(text, text_rect)

    #display directions
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

        pygame.display.update()

        #event listener loop
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                sys.exit()

            #listen for mouse click
            elif event.type == pygame.MOUSEBUTTONUP:
                x,y = pygame.mouse.get_pos()

                #if user clicks in text box
                if(x>=50 and x<=900 and y>=200 and y<=750):
                    isActive = True #start game & time
                    input_text = ''
                    start = time.time()

                #if users clicks reset button
                if(x>=310 and x<=510 and y>=390 and end):

                    #reset function vars
                    user_input = ''
                    word = ''
                    start = 0
                    totalTime = 0
                    wpm = 0
                    isActive = False
                    reset = False
                    end = False

                    #grab new rando sentence
                    file = open('sentences.txt').read()
                    sentences = file.split('\n')
                    word= random.choice(sentences)

                    #reset play background
                    background = pygame.image.load('play.png')
                    background = pygame.transform.scale(background, (w, h))

                    screen.fill((240,240,240))
                    screen.blit(background, (0,0))

                    #reset text box
                    pygame.draw.rect(screen,(102,255,243), (50,300,900,100), 2)

                    #draw button again 
                    backButton.draw(screen)

                    #display new sentence
                    font = pygame.font.Font(None, 24)
                    text = font.render(word, 1,(240,240,240))
                    text_rect = text.get_rect(center=(1000/2, 275))
                    screen.blit(text, text_rect)

                    #display directions
                    font = pygame.font.Font(None, 21)
                    text = font.render("Click box to type", 1,(240,240,240))
                    text_rect = text.get_rect(center=(500, 415))
                    screen.blit(text, text_rect)
                    pygame.display.update()
                    x,y = pygame.mouse.get_pos()

            #listens for key press
            elif event.type == pygame.KEYDOWN:
                #if game is cur active & not over
                if isActive and not end:
                    #if return key is pressed
                    if event.key == pygame.K_RETURN:

                        #to terminal
                        print(user_input)

                        #get results and stats of play
                        if not end:
                            #calc total time took
                            totalTime = time.time() - start

                            #determine percent chars correct
                            count = 0
                            for i, char in enumerate(word):
                                try:
                                    if user_input[i] == char:
                                        count +=1
                                except:
                                    pass
                            percent = count/len(word)*100

                            #determine words typed per minute
                            wpm = len(user_input)*60/(5*totalTime)

                            #set game to over
                            end = True

                            #send stats in db
                            with sql.connect("speedyfingersDB.db") as con:
                                cur = con.cursor()
                                #query for Stats
                                cur.execute("INSERT INTO Stats (totalTime,wpm,percent) VALUES (?,?,?)", (totalTime,wpm,percent) )
                                con.commit()
                            con.close() #close connections

                            #show reset button
                            results = "Time: " + str(round(totalTime)) + " secs   Percent: " + str(round(percent)) + "%" + "   WPM: " + str(round(wpm))
                            again = pygame.image.load('playagain.png')
                            again = pygame.transform.scale(again, (150,150))
                            screen.blit(again, (500-75, 750-250))
                        #to terminal
                        print(results)

                        #display stats to user
                        font = pygame.font.Font(None, 28)
                        text = font.render(results, 1,(240, 240, 240))
                        text_rect = text.get_rect(center=(500, 450))
                        screen.blit(text, text_rect)

                        #game over
                        end = True
                        pygame.display.update()

                    #if key is backspace delete user input
                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]

                    else:
                        try:
                           user_input += event.unicode
                        except:
                           pass

            #if user presses main menu button
            elif backButton.is_clicked(event):
                mainMenu(screen, 1000, 750)

    #clock by seconds
    clock.tick(60)

# directions screen
def directions(screen):

    #set directions background image
    background = pygame.image.load('directions.png')
    background = pygame.transform.scale(background, (1000, 750))

    screen.fill((0,0,0))
    screen.blit(background, (0,0))

    #create back button
    backButton = Button((150, 600), (200, 90), (240, 240, 240), "Back to Main")

    #create & display intro & 3 directions
    directions = "Welcome to the best game ever: SpeedyFingers!!" 
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

    #draw button and text
    backButton.draw(screen)
    pygame.display.update()

    #event listener loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #if back button is pressed -> mainmenu
            elif backButton.is_clicked(event):
                print("back button pressed")
                mainMenu(screen, 1000, 750)

#stats screen
def stats(screen):

    #connect to db
    con = sql.connect("speedyfingersDB.db")
    con.row_factory = sql.Row
    cur = con.cursor()

    #query executed
    cur.execute('select * from Stats ORDER BY percent DESC, wpm DESC, totalTime ASC  LIMIT 5')

    #get results
    rows = cur.fetchall()

    #gather row cells into one sentence & put in list
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

    #set background to stats image
    background = pygame.image.load('stats.png')
    background = pygame.transform.scale(background, (1000, 750))

    screen.fill((0,0,0))
    screen.blit(background, (0,0))

    #create back button
    backButton = Button((75, 600), (200, 90), (98, 219, 200), "Back to Main")

    #display screen text
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

    #display list of results row by row
    row = 400
    font1 = pygame.font.Font(None, 30)
    for res in results:
        text1 = font1.render(res, 1,(105,105,105))
        screen.blit(text1, (395, row))
        row += 50

    #draw button & update screen
    backButton.draw(screen)
    pygame.display.update()

    #event listener loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif backButton.is_clicked(event):
                print("back button pressed")
                mainMenu(screen, 1000, 750)

#Button class
class Button(object):
    #constructor
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

    #draw button function
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    #if clicked function
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)


#Button Image Class
class ButtonImage(object):
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self, screen):
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



#call to main to play :)
main()
