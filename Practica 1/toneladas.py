toneladas_cereal= [12,24,16,15,20,18,6,10,12,11,15,12]
toneladas_mayores = []
toneladas_menores = []

suma = 0
for x in toneladas_cereal:
    suma += x
promedio = suma / len(toneladas_cereal)

for i in toneladas_cereal:
    if i > promedio:
        toneladas_mayores.append(i)
    else:
        toneladas_menores.append(i)

print("El promedio es= ", promedio)
print("Los meses que tuvieron cosecha superior al promedio fueron = ",len(toneladas_mayores))
print("Los meses que tuvieron cosecha inferior al promedio fueron = " ,len(toneladas_mayores))
