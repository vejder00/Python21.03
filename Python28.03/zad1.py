 #!/usr/bin/env python
 #encoding: utf-8
import sys

linia = 'Ala ma kota'

width = 5

for index in range(0,len(linia), width):
    print(linia[index:index+width].center(width))


 
