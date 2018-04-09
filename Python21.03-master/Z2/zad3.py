 import sys
slownik = {}
with open(sys.argv[1],"r") as plik:
    for linia in plik:
        for slowo in linia.split():
            if(slowo in slownik):
                slownik[slowo] +=1
            else:
                slownik[slowo] = 1
                
print slownik