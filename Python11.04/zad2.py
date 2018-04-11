#!/usr/bin/env python
#encoding: utf-8

import re

class MailException(Exception):
    pass


mailik = r'\w+@(\w+).pl'

class Maile:
    def __init__(self, adres):
        try:
            re.compile(mailik)
            re.match(adres)
        except TypeError:
            print('Zly adres emial')
        else:
            print ('Dodano')

        


x=Maile('ziom@o2.pl')
y=Maile('2')
