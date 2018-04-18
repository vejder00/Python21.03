#!/usr/bin/env python
#encoding: utf-8

import sqlite3
connection = sqlite3.connect('biblioteka.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS ksiazki(id integer, tytul text, autor text, rok_Wydania integer) ''')

cursor.execute('''INSERT INTO ksiazki IF NOT EXIST VALUES (1,'Harry Potter','J.K.Rowllig',1992)''')
cursor.execute('''INSERT INTO ksiazki VALUES (2,'Pan Tadeusz','Adam Mickiewicz',1834)''')


connection.commit()

for row in cursor.execute('SELECT * FROM ksiazki'):
    print(row)
    
    

connection.close()
