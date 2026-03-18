class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cola = [None] * capacidad
        self.frente = -1
        self.final = -1

    def esta_vacia(self):
        return self.frente == -1
    
    def esta_llena(self):
        return (self.final + 1) % self.capacidad == self.frente
    
    def encolar(self, dato):
        if self.esta_llena():
            print("La cola está llena")
            return
        
        if self.esta_vacia():
            self.frente = 0
            self.final = 0
        else: 
            self.final = (self.final + 1) % self.capacidad

        self.cola[self.final] = dato

    def descolar(self):
        if self.esta_vacia():
            print("La cola está vacía")
            return None                
        dato = self.cola[self.frente]

        if self.frente == self.final:
            self.frente = -1
            self.final = -1
        else: 
            self.frente = (self.frente + 1) % self.capacidad

        return dato    
    
    def ver_frente(self):
        if self.esta_vacia():
            return None
        return self.cola[self.frente]
    
    def mostrar(self):
        if self.esta_vacia():
            print("Cola vacía")
            return
        
        elementos = []
        i = self.frente

        while True:
            elementos.append(self.cola[i])
            if i == self.final:
                break
            i = (i + 1) % self.capacidad

        print("Cola:", elementos)



cola_turnos = ColaCircular(5)


print("Insertando turnos A01, A02, A03")
cola_turnos.encolar("A01")
cola_turnos.encolar("A02")
cola_turnos.encolar("A03")



cola_turnos.mostrar()


print(f"Atendiendo turno: {cola_turnos.descolar()}")
print(f"Atendiendo turno: {cola_turnos.descolar()}")


cola_turnos.mostrar()


print("Insertando turnos A04, A05, A06, A07")

cola_turnos.encolar("A04")
cola_turnos.encolar("A05")
cola_turnos.encolar("A06")
cola_turnos.encolar("A07")


cola_turnos.mostrar()


if cola_turnos.esta_llena():
    print("La cola está llena")