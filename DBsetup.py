import sqlite3
import pandas as pd

#Connect to database
conn = sqlite3.connect('speedyfingersDB.db')
cur = conn.cursor()


###################### CREATE SQL TABLE FROM EXCEL, USE IN CASE OF DELETING DATABASE  ###################

# stories = pd.read_excel('children_stories.xlsx',sheet_name='childrenStories',header=0)
# conn.execute('CREATE TABLE IF NOT EXISTS Stories(id INTEGER PRIMARY KEY AUTOINCREMENT, StoryName VARCHAR(150),Story VARCHAR(8000))')
# stories.to_sql('Stories', conn, if_exists = 'append', index=False)

#########################################################################################################

#Basic Table Creation

conn.execute('CREATE TABLE IF NOT EXISTS Users (userID INTEGER PRIMARY KEY AUTOINCREMENT,userName VARCHAR(100) NOT NULL, highScore FLOAT,avgScore FLOAT);')
print("Users table created succesfully")
conn.execute('CREATE TABLE IF NOT EXISTS Attempts(userID INT,textID INT,score FLOAT,attemptTime DATETIME DEFAULT CURRENT_TIMESTAMP,succesfullKeys INT,missedKeys INT);')
print("Attempts table created succesfully")







############################################ USEFUL QUERIES #############################################################


#Example of adding new user into table
# name = "Diego"
# cur.execute("INSERT INTO Users (userName, highScore, avgScore) SELECT ?,?,? WHERE NOT EXISTS(SELECT * FROM Users WHERE userName = ?)", (name,0,0,name))
# conn.commit()

#Getting results from table
# cur.execute("SELECT * FROM Stories WHERE id = '4'")
# table = cur.fetchall()
# print(table)


#Delete all entries of a table
# cur.execute("DELETE FROM Users")
# conn.commit()

#Store value in variable from query result
# cur.execute("SELECT userName FROM Users WHERE userID = '1'")
# user = cur.fetchone()[0]
# print("Current user is = " + user)





