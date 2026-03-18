from collections import deque

bicola = deque()
Tarea = ["T1","T2","T3","T4","T5","T6"]
Fallos = [1,0,2,1,2,2]
intentos_Iniciales = [0,0,0,0,2,1]

for x in range(6):
    bicola.append([Tarea[x], Fallos[x], intentos_Iniciales[x]])

