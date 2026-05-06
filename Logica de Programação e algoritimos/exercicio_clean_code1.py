numeros = []

for i in range(5):
    numeros.append(float(input(f"Digite a {i+1}ª número: ")))

soma = sum(numeros)
print ("total", soma)

