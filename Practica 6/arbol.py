class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecha = None


    def insertar(self, nodo, lista):
        if not lista:
            return
        dato_actual = lista[0]

        if dato_actual != nodo.dato:
            actual = nodo
            while True:
                if dato_actual < actual.dato:
                    if actual.izquierdo is None:
                        actual.izquierdo = Nodo(dato_actual)
                        break
                    else:
                        actual = actual.izquierdo
                else:
                    if actual.derecha is None:
                        actual.derecha = Nodo(dato_actual)
                        break
                    else:
                        actual = actual.derecha
        self.insertar(nodo, lista[1:])

    
    def preorden(self, nodo):
        if nodo:

            print(nodo.dato, end=" ")
            if nodo.izquierdo is not None or nodo.derecha is not None:
                self.preorden(nodo.izquierdo)
                self.preorden(nodo.derecha)
        else:

            print("None", end=" ")

    def inorden(self, nodo):
        if nodo:
            if nodo.izquierdo is not None or nodo.derecha is not None:
                self.inorden(nodo.izquierdo)
            print(nodo.dato, end=" ")
            if nodo.izquierdo is not None or nodo.derecha is not None:
                self.inorden(nodo.derecha)
        else:
            print("None", end=" ")

    def postorden(self,nodo):
        if nodo:
            if nodo.izquierdo is not None or nodo.derecha is not None:
                self.postorden(nodo.izquierdo)
                self.postorden(nodo.derecha)
            print(nodo.dato, end=" ")
        else:
            print("None", end=" ")


datos = [3, 1, 2, 4, 5]
raiz = Nodo(datos[0])

raiz.insertar(raiz, datos)

print("Preorden:"); raiz.preorden(raiz)
print("\nInorden:"); raiz.inorden(raiz)
print("\nPostorden:"); raiz.postorden(raiz)


