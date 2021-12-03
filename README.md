# speedyfingers

## Execute
Download zip from github  
`$ pip install necessary libraries`

`$ sudo apt install sqlite3`

`$ python3 newSpeedy.py`

- program creates a database called speedyfingersDB.db when command above is executed, to clear DB delete file


## Description
a speed typing application/game for users to test, improve, and challenge their keyboard typing abilities 

## Group Members
1. Sophie Pavia
2. Alessandra Carbonel
3. Diego De Saint Malo

## Libraries
- pygame
- pygame.freetype
- button
- sys
- time
- random
- sqlite3
- from difflib import SequenceMatcher

## Resources
https://www.pygame.org/docs/
For button class: https://stackoverflow.com/questions/47981842/how-do-i-create-a-pygame-with-multiple-menus
## Added Features 
We implemented the main goals of our project proposal for having the modes play, check stats, and look at directions

## Seperation of Work
- Sophie:Project plan, overall logic, play mode,stat mode, directions mode, graphics, database connection & query, overall code functionality
- Alessandra:project plan, intro screen, arrow button, overall logic, play mode, stat mode, directions mode, graphics, database connection & query 
- Diego:project plan, inital skelton of project, Button Class, database creation (DBsetup.py), function set up, text color change as user types

## Bugs/Obstacles Faced
Due to time constraints there is only one level of 'play' (one level of difficulity). We also only went with using one DB for storing user stats instead of one for user stats, another for storing sentences. We no longer use pandas library (said in status report 2). 

## GitHub Link
https://github.com/sophiepavia/speedyfingers


