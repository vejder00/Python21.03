#!/usr/bin/env python
#encoding: utf-8

import math

def pierw(x):
    try:
        x = int(x)
        result = math.sqrt(x)
    except TypeError:
        print('Podales zly typ zmiennej')
    except NameError:
        print('Tu jest nameerror')
    except ValueError:
        print('Podales zla wartosc')
    else:
        print(result)
        

liczba = raw_input('Podaj liczbe :')
pierw(liczba)
        
