from collections import deque

bicola = deque()
Tarea = ["T1", "T2", "T3", "T4", "T5", "T6"]
Fallos = [1, 0, 2, 1, 2, 2]
intentos_Iniciales = [0, 0, 0, 0, 2, 1]

for x in range(6):
    bicola.append([Tarea[x], Fallos[x], intentos_Iniciales[x]])

print("=== ESTADO INICIAL DE LA BICOLA DE TAREAS ===")
for t in bicola:
    print(f"Tarea: {t[0]} | Fallos: {t[1]} | Intentos Previos: {t[2]}")
print("=============================================\n")

print("--- PROCESANDO TAREAS ---")

while len(bicola) > 0:
    tarea_actual = bicola.popleft()
    nombre, fallos, intentos = tarea_actual
    
    print(f"Procesando {nombre}...")
    
    if fallos == 0:
        print(f" -> ¡{nombre} completada con éxito a la primera!")
    
    elif fallos == 1:
        intentos += 1
        print(f" -> {nombre} tuvo un fallo. Se reencola al FINAL (Por la derecha). Intentos actuales: {intentos}")
        bicola.append([nombre, 0, intentos])
        
    elif fallos >= 2:
        intentos += 1
        print(f" -> ¡ALERTA! {nombre} tiene muchos fallos ({fallos}). Reencolando al INICIO con alta prioridad.")
        bicola.appendleft([nombre, fallos - 1, intentos])
        
    print(f" Estado de la bicola: {[t[0] for t in bicola]}\n")

print("=============================================")
print("¡Todas las tareas han sido procesadas con éxito!")
print("=============================================")