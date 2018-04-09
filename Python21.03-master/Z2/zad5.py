#!/usr/bin/env python
#encoding: utf-8

import sys

with open(sys.argv[1],"r") as plik:
    plik2= open(sys.argv[2],"w")
    for linia in plik:
        for znak in linia.len():
            znak= znak+3
            plik2.write(znak)

plik2.close()
    
