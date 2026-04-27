def mi_dijkstra(nodo_inicio):
    grafo = {
        0: {1: 9, 4: 6},
        1: {0: 9, 3: 8},
        2: {4: 5, 5: 6},
        3: {1: 8, 5: 1, 7: 7},
        4: {0: 6, 2: 5, 6: 3},
        5: {2: 6, 3: 1},
        6: {4: 3, 7: 2},
        7: {3: 7, 6: 2}
    }

    nodos = [0, 1, 2, 3, 4, 5, 6, 7]
    conocido = [False] * 8
    costo = [float('inf')] * 8
    camino_previo = [-1] * 8

    costo[nodo_inicio] = 0

    for _ in range(8):
        mejor_distancia = float('inf')
        u = -1
        
        for n in nodos:
            if not conocido[n] and costo[n] < mejor_distancia:
                mejor_distancia = costo[n]
                u = n

        if u == -1:
            break

        conocido[u] = True

        vecinos = grafo[u]
        for v in vecinos:
            peso_arista = vecinos[v]
            if costo[u] + peso_arista < costo[v]:
                costo[v] = costo[u] + peso_arista
                camino_previo[v] = u

    print("Vertex   Known   Cost    Path")
    for n in nodos:
        valor_k = "T" if conocido[n] else "F"
        
        # Reconstrucción del camino recorrido
        ruta = []
        actual = n
        while actual != -1:
            ruta.insert(0, str(actual))
            actual = camino_previo[actual]
        
        camino_str = " ".join(ruta)
        
        print(f"{n}        {valor_k}       {costo[n]}      {camino_previo[n]}      {camino_str}")

mi_dijkstra(0)