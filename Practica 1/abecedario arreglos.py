cadena = "Parangaricutirimicuaro"
abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
abecedario_mayuscula = []


for i in abecedario:
    abecedario_mayuscula.append(i.upper())

for z in abecedario_mayuscula:
    if cadena.count(z) != 0:
        print(z," =",cadena.count(z))

for x in abecedario:
    if cadena.count(x) != 0:
        print(x," =",cadena.count(x))