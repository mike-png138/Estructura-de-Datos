class Pila:
    def __init__(self):
        self.pila = []
        self.top = 0

    def push(self,elemento):
        self.pila.append(elemento)

    def pop(self):
        if not self.pila_vacia():
            return self.pila.pop()
        else:
            return "pila vacia"
        
    def peek(self):
        if not self.pila_vacia():
            ultimo_elemento = len(self.pila) - 1
            return self.pila[ultimo_elemento]
        else:
            return "pila vacia"
        
    def pila_vacia(self):
        return len(self.pila) == 0
    
    def size(self):
        return len(self.pila)



