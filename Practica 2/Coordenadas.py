matriz = [[4,7,2,9,5,7],
          [1,3,7,6,8,0],
          [9,2,5,7,4,6],
          [8,7,1,3,7,2],
          [5,0,6,4,2,9],
          [7,8,9,2,1,7]]


def buscar (valor):
    busqueda = []
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == valor:
                busqueda.append((i+1,j+1))

    if len(busqueda) > 0:
        return busqueda
    else:
        return "No Encontrado"
    

valores =  [7, 2, 9, 0, 4, 1, 6, 8, 3, 10]
for i in valores:
    resulado = buscar(i)
    print(f"Las coordenadas de {i}: son: ")
    print(resulado)
    print("-------------------------------------------")