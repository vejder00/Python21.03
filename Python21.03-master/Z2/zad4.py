 import sys

if sys.argv[1] == "-":
    linia = raw_input()
    znak = ""
    while linia != znak:
        if linia.find(sys.argv[2])>-1:
            print (linia)
        linia = raw_input()
    linia = ""
else:
    with open(sys.argv[1],"r") as plik:
	if linia.find(sys.argv[2])>-1:
                print linia