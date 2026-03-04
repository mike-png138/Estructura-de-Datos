def enque_head(lista, elemento):
    lista.insert(0, elemento)

def deque_head(lista):
    return lista.pop(0)

def enque_tail(lista, elemento):
    lista.append(elemento)

def deque_tail(lista):
    return lista.pop()

def retiros(saldo, retiro):
    monto_retiro = deque_head(retiro)
    saldo_actual = deque_head(saldo)

    nuevo_saldo = saldo_actual - monto_retiro
    enque_tail(saldo, nuevo_saldo)

def depositos(saldo, deposito):
    monto_deposito = deque_tail(deposito)
    saldo_actual = deque_head(saldo)

    nuevo_saldo = saldo_actual + monto_deposito
    enque_tail(saldo, nuevo_saldo)

saldo = [1000,1000,1000,1000,1000]
retiro = [500,500,500,500,500]
deposito = [300,300,300,300,300]

print(f"Los saldos son: {saldo}")

for _ in range(5):
    retiros(saldo, retiro)
print(f"Saldo despues del retiro: {saldo}")

for _ in range(5):
    depositos(saldo, deposito)
print(f"Saldo despues del deposito: {saldo}")

