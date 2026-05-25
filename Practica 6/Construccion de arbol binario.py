class NodoArbol:
    def __init__(self,clave, valor, izquierdo=None, derecho=None, padre=None):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre

    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        return not self.padre

    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self

class armadoArbol:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, clave):
        if self.raiz is None:
            self.raiz = NodoArbol(clave, clave)
        else:
            self._insertar_recursivo(clave, self.raiz)

    def _insertar_recursivo(self, clave, nodo_actual):
        if clave < nodo_actual.clave:
            if nodo_actual.tieneHijoIzquierdo():
                self._insertar_recursivo(clave, nodo_actual.hijoIzquierdo)
            else:
                nodo_actual.hijoIzquierdo = NodoArbol(clave, clave, padre = nodo_actual)
        else:
            if nodo_actual.tieneHijoDerecho():
                self._insertar_recursivo(clave, nodo_actual.hijoDerecho)
            else:
                nodo_actual.hijoDerecho = NodoArbol(clave, clave, padre=nodo_actual)

    def mostrar_estructurado(self, nodo_actual, nivel=0):
        if nodo_actual is not None:
            self.mostrar_estructurado(nodo_actual.hijoDerecho, nivel + 1)
            
            print("    " * nivel + f"-> {nodo_actual.clave}")
            
            self.mostrar_estructurado(nodo_actual.hijoIzquierdo, nivel + 1)

    

datos = [3,1,2,4,5]

datos_unicos = []
for n in datos:
    if n not in datos_unicos:
        datos_unicos.append(n)

mi_arbol = armadoArbol()
for numero in datos_unicos:
    mi_arbol.insertar(numero)

print("ARBOL BINARIO ESTRUCTURADO:")
print("=" * 30)
mi_arbol.mostrar_estructurado(mi_arbol.raiz)
print("=" * 30)

