calificaciones = [8,8,7,5,10,9,9,5,6,10]
aprobados = []
reprobados = []
calificacion_mayor = []
suma = 0
for x in calificaciones:
    suma = suma + x
    if x > 5:
        aprobados.append(x)
    else:
        reprobados.append(x)
    if x >= 8:
        calificacion_mayor.append(x)

promedio = suma / len(calificaciones)

print("El promedio general del grupo es: ", promedio)
print("El numero de aprobados es:",len(aprobados))
print("El numero de reprobados es:",len(reprobados))
print("El porcentaje de alumnos aprobados es:",(len(aprobados) / 10 * 100),"%")
print("El porcentaje de alumnos reprobados es:",(len(reprobados) / 10 * 100),"%")
print("Alumnos con calificacion igual o mayor a 8: ",len(calificacion_mayor))
