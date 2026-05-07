from collections import deque

def bfs_personalizado(graph, start_node):
    queue = deque([start_node])
    visited = {start_node}
    atendidos = []
    
    print(f"Recorriendo Grafo de Usuario desde: {start_node}")
    
    while queue:
        
        print(f"Cola{list(queue)}")
        
        current_node = queue.popleft()
        
        atendidos.append(current_node)
        
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
        


    print(f"Lista final de elementos atendidos: {atendidos}")

grafo_usuario = { 
    'A': ['B', 'C'], 
    'B': ['D', 'E'], 
    'C': ['F', 'G'], 
    'D': [], 
    'E': [], 
    'F': [],
    'G': []
}

bfs_personalizado(grafo_usuario, 'A')