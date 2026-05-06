matriz = [
    [3,6]
    [9,12]
]
resultado = 0 
for i in range (2):
    for j in range(2):
        if matriz [i][j] >5:
            resultado += matriz[i][j]
        else:
            resultado -= 1
print(resultado)