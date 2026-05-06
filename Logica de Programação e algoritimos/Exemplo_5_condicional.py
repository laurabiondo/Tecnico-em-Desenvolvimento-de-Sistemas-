idade = int(input ("Digite sua idade: "))
carteira = input ("Você tem CNH?: ")

if (idade >= 18 and carteira == "SIM"):
    print ("Você pode dirigir!")

elif (idade >=18 and carteira == "NÃO"):
    print ("Você não pode dirigir!")

elif (idade < 18):
    print("Você não pode dirigir!")

else:
    print ("ERRO")