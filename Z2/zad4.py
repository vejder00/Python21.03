#!/usr/bin/env python
#encoding: utf-8

import re
import sys


pesel=re.compile(
    r'''(
        ?P<Rok urodzenia: 19> \d\d
        (?P<Miesiac urodzenia> ((1[0-2]) | (0[1-9])))
        (?P<Dzien urodzenia> (0[1-9])|(1[0-9])|(2[0-9])|(3[0-1]))
    )''',
    re.IGNORECASE | re.VERBOSE
)
    
with open('xd',"r") as plik:
        for linia in plik:
            for adres in pesel.finditer(linia):
                print adres.groupdict()

    

#ta wersja w komentarzu zapobiega wyjsciu poza zakres
# (?P<adres> (([0-1][
