from collections import deque
bicola = deque(maxlen=3)
peticiones = [1,2,3,4,5]
tiempo = [0,2,4,6,12]
cont = 0

for i, peticiones in enumerate(peticiones):
    if tiempo[i] <= 10 and cont < 3:
        bicola.append(peticiones)
        print(bicola)
        cont += 1
    elif tiempo[i] <= 10 and cont >= 3:
        bicola.popleft()
        bicola.appendleft(peticiones)
        print(bicola)
        bicola.popleft()
        bicola.append(peticiones)
    elif tiempo[i] > 10:
        for y in range(2):
            print(bicola)
            bicola.popleft()
        print(bicola)
        bicola.pop()
        print(bicola)
        bicola.append(peticiones)
        print(bicola)
