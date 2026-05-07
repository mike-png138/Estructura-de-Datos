calificaciones_repetidas = [1,2,4,4,4,5,7,9,11,11,13,14,15,15,16,16]
calificaciones = []
for i in range(len(calificaciones_repetidas)):
    if calificaciones_repetidas[i] != calificaciones_repetidas[i - 1]:
        calificaciones.append(calificaciones_repetidas[i])

print(calificaciones)