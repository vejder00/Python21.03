 #!/usr/bin/env python
 #encoding: utf-8
 
import re


ip=re.compile(
    r'''(
        (?P<adres>\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d)
    )''',
    re.IGNORECASE | re.VERBOSE
)
    
with open('xd',"r") as plik:
        for linia in plik:
            for adres in ip.finditer(linia):
                print adres.groupdict()

    

#ta wersja w komentarzu zapobiega wyjsciu poza zakres
# (?P<adres> (([0-1][0-9][0-9])|(2[0-4][0-9])|(25[0-5]))\.(([0-1][0-9][0-9])|(2[0-4][0-9])|(25[0-5]))\.(([0-1][0-9][0-9])|(2[0-4][0-9])|(25[0-5]))\.(([0-1][0-9][0-9])|(2[0-4][0-9])|(25[0-5])))