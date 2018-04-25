#!/usr/bin/env python

import subprocess
import os

def fun(liczba):
    tab = []
    k = 2
    i = 0
    ile = 0
    while liczba>1:
        if liczba%k == 0:
            ile = ile + 1
            liczba = liczba/k
            if liczba == 1:
                tab.append((k,ile))
        else:
            if ile>0:
                tab.append((k,ile))
                ile = 0
            k = k + 1
                
    for x in tab:
        print x

fun(756)
                
            
