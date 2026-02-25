Matriz = [[0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0]]


def RESERVAR(i,j):
    if Matriz[i - 1][j - 1] == 0:
        Matriz[i - 1][j - 1] = 1
        return "OK: reservado"
    else:
        return "RECHAZO: ocupado"

def LIBERAR(i,j):
    if Matriz[i - 1][j - 1] == 1:
        Matriz[i - 1][j - 1] = 0
        return "OK: Liberado"
    else:
        return "RECHAZO: ya libre"

def CONSULTAR(i,j):
    if Matriz[i - 1][j - 1] == 1:
        return "Estado = Reservado"
    else:
        return "Estado = Libre"



print(RESERVAR(1,1))
print(RESERVAR(1,2))
print(RESERVAR(1,1))
print(CONSULTAR(1,1))
print(LIBERAR(1,1))
print(LIBERAR(1,1))
print(RESERVAR(3,4))
print(RESERVAR(6,6))
print(CONSULTAR(6,6))
print(RESERVAR(2,5))

cont = 0

for i in range(len(Matriz)):
    for x in range(len(Matriz)):
        if Matriz[i][x] == 1:
            cont += 1

print(f"Los asientos reservados son: {cont}")

reservasMax = -1
cont = -1

for i in range(len(Matriz)):
    contFila = Matriz[i].count(1)
    if contFila > cont:
        cont = contFila
        filasMasReservadas = i + 1
        
print(f"La fila con mas asientos es: {filasMasReservadas}")
           


