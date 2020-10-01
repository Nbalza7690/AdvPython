
import sqlite3

# Files to grab from and put into the database
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

conn = sqlite3.connect('assignment.db')

# Create the table with an ID number and a single column
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_data TEXT)")
    conn.commit()
conn.close()

conn = sqlite3.connect('assignment.db')
cur = conn.cursor()

def data_entry():
    for item in fileList:
        if item.endswith('.txt'):
            cur.execute("INSERT INTO tbl_files(col_data) VALUES(?)", (item,))
        conn.commit()

data_entry()

# Querry the database

conn = sqlite3.connect('assignment.db')
cur = conn.cursor()

cur.execute ('SELECT col_data FROM tbl_files')
varFile = cur.fetchall()
for item in varFile:
    prntDB = '.txt File: {}'.format(item[0])
    print(prntDB)


