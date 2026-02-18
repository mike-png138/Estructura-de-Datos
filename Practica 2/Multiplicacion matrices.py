
A = [[5,6,13],[3,10,1],[2,11,3]]
B = [[1,2,17],[6,5,15],[3,11,12]]
C = [[0,0,0],[0,0,0],[0,0,0]]
suma = 0

for i in range(len(A[0])):
    for j in range(len(A[0])):
        for k in range(len(A[0])):
            suma += A[i][k] * B[k][j]
        C[i][j] = suma
        suma = 0
print(C)