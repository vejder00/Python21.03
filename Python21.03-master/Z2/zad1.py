napis = """k1:w1
k2:w2
k3:w3"""
 
slownik = {
    }
 
lista = napis.split("\n")
 
for linia in napis.splitlines():
    element = linia.split(":")
    
    slownik[element[0]] = element[1]
    
print slownik