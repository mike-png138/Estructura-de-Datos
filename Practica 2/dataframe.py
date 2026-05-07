import pandas as pd

#Leer archivo CSV delimitado por comas (por defecto)
df = pd.read_csv('Practica 2/Housing.csv')

price = list(df['price'])
bedrooms = list(df['bedrooms'])
bathrooms = list(df['bathrooms'])
sqft_living = list(df['sqft_living'])
sqft_lot = list(df['sqft_lot'])
floors = list(df['floors'])
sqft_above = list(df['sqft_above'])
sqft_basement = list(df['sqft_basement'])
yr_built = list(df['yr_built'])



def calcular(nombre):

    #media
    suma = 0
    for x in nombre:
        suma += x
    media = suma / len(nombre)
    print(f"La media es {media}")

   #moda 
    conteo = {}
    for x in nombre:
        if x in conteo:
            conteo[x] = conteo[x] + 1
        else:
            conteo[x] = 1

        
        max_apariciones = 0
        moda = 0

        for j in conteo:
            
            if conteo[j] > max_apariciones:
                max_apariciones = conteo[j]
                moda = j

    print(f"La moda es: {moda}")

    #media
    suma_varianza = 0
    for x in nombre:
        diferencia = x - media
        cuadrado = diferencia ** 2
        suma_varianza = suma_varianza + cuadrado

    varianza = suma_varianza / len(nombre)

    print(f"La varianza es: {varianza}")
    #desviacion estandar 
    desviacion_estandar = varianza ** 0.5
    print(f"La desviacion estandar es {desviacion_estandar}")
    print("--------------------------------------")

calcular(price)
calcular(bedrooms)
calcular(bathrooms)
calcular(sqft_living)
calcular(sqft_lot)
calcular(floors)
calcular(sqft_above)
calcular(sqft_basement)
calcular(yr_built)




    





