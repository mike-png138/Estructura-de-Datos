def torres_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return
    
    # Paso 1: Mover n-1 discos del origen al auxiliar
    torres_hanoi(n - 1, origen, auxiliar, destino)
    
    # Paso 2: Mover el disco más grande al destino
    print(f"Mover disco {n} de {origen} a {destino}")
    
    # Paso 3: Mover los n-1 discos del auxiliar al destino
    torres_hanoi(n - 1, auxiliar, destino, origen)

# Ejecución para 5 discos
n_discos = 4
torres_hanoi(n_discos, 'A', 'C', 'B')