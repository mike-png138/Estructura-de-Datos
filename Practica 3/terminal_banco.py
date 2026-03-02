def enque(lista, elemento):
    lista.append(elemento)

def deque(lista, lista2):
    enque(lista2,(lista[0]))
    lista.pop(0)

def peek(lista):
    return lista[0]

def retiros(lista, lista2):
    r = lista[0] - lista2[0]
    deque(lista,lista2)
    enque(lista, r)

def deposito(lista, lista2):
    d = lista[0] + lista2[0]
    deque(lista, lista2)
    enque(lista,d)

saldo = []
retiro = []
depositos = []

enque(saldo,1000)
enque(saldo,1000)
enque(saldo,1000)
enque(saldo,1000)
enque(saldo,1000)

enque(retiro, 500)
retiros(saldo, retiro)
retiros(saldo, retiro)
retiros(saldo, retiro)
retiros(saldo, retiro)
retiros(saldo, retiro)
print(saldo)

enque(depositos,300)
deposito(saldo, depositos)
deposito(saldo, depositos)
deposito(saldo, depositos)
deposito(saldo, depositos)
deposito(saldo, depositos)
print(saldo)





