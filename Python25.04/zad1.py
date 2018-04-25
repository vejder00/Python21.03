#!/usr/bin/env python

import subprocess
import os

subprocess.call(['g++','p1.cpp','-o','p1.out'], shell=False)
with open(os.devnull, 'w') as devnull:
    exCode = subprocess.call(['./test.out'], stdout=devnull, shell=False)
    if exCode == 0:
        print("Udalo sie!")
    else:
        print("Blad!")
