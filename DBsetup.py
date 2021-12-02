import sqlite3
import pandas as pd

#Connect to database

def createDB():
    conn = sqlite3.connect('speedyfingersDB.db')
    conn.execute('CREATE TABLE IF NOT EXISTS Stats(totalTime int, wpm int, percent int)') 
    print("Attempts table created succesfully")
    conn.close()




