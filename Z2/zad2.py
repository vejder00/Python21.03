#!/usr/bin/env python
#encoding: utf-8

import sys
with open(sys.argv[1],"r") as f:
    napis = f.read()
slownik = {}
for linia in filter(None,napis.splitlines()):
    element = linia.split(":")
    slownik[element[0]]=element[1]
    
print slownik
