#!/usr/bin/env python
#encoding: utf-8

import sqlite3
connection = sqlite3.connect('biblioteka.db')

cursor = connection.cursor()

cursor.execute('''INSERT INTO ksiazki VALUES (2,'Pani Bogusia','Adam Mickiewicz',1834)''')



for row in cursor.execute('SELECT * FROM ksiazki'):
    print(row)

print '--------------------------'
connection.rollback()
for row in cursor.execute('SELECT * FROM ksiazki'):
    print(row)
    
connection.commit()
    

connection.close()

