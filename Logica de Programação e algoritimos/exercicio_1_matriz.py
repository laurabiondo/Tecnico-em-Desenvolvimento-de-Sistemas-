matriz_1 = []
matriz_2 = []
matriz_soma = []

#PREENCHER MATRIZ (REPETIR SEMPRE QUE PREENCHER MATRIZ)
for i in range(3):
    linha = []
    for j in range (3):
        linha.append(int(input(f"Matriz_1[{i}][{j}]=")))
    matriz_1.append(linha)

#PREENCHER MATRIZ (REPETIR SEMPRE QUE PREENCHER MATRIZ)
for i in range(3):
    linha = []
    for j in range (3):
        linha.append(int(input(f"Matriz_2[{i}][{j}]=")))
    matriz_2.append(linha)

#PREENCHER MATRIZ (REPETIR SEMPRE QUE PREENCHER MATRIZ)
for i in range(3):
    linha = []
    for j in range (3):
        linha.append(matriz_1[i][j]+matriz_2[i][j])
    matriz_soma.append(linha)

#EXIBIR MATRIZ (REPETIR SEMPRE QUE EXIBIR MATRIZ)
print("Soma é igual a: ")
for linha in matriz_soma: 
    print(linha)
    



