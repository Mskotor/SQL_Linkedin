import sqlite3


# << Connect to the database >>
database = sqlite3.connect('WSDA_Music.db')

# << Create a cursor object >>
cursor = database.cursor()

