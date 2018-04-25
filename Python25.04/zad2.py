#!/usr/bin/env python

import subprocess
import os

linia = '  '
tabCount = len(linia) - len(linia.lstrip(' '))
print(tabCount)


kat = '''
K1
 K2
 K3
  K4
K5
 k6'''

while linia in kat:
    linia= kat.readline()
    #NIEDOKOŃCZONE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
