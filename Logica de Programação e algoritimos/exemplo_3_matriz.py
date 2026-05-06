linhas = int(input("Quantidades de linhas (i): "))
colunas = int(input("Quantidades de linhas (i): "))
matriz = []

for i in range(linhas):
    linha = []
    for j in range (colunas):
        linha.append(int(input(f"M[{i}][{j}]=")))
    matriz.append(linha)

print("Matriz preenchida: ")
for linha in matriz: 
    print(linha)