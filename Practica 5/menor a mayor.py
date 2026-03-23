from Pila import Pila

cola = [12500.0,11890.0,13010.35,14100.0,13650.8,14999.99,
        15800.0,16250.25,15120.0,14780.4,13999.0,1550.75]

mi_pila = Pila()

while len(cola) > 0:
    menor = cola.pop(0) 
    
    for _ in range(len(cola)):
        siguiente = cola.pop(0) 
        
        if siguiente < menor:
            cola.append(menor)
            menor = siguiente
        else:
            cola.append(siguiente)
            
    mi_pila.push(menor)

print("Pila ordenada (el último en entrar fue el más grande):")
print(mi_pila.pila)