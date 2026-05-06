ValorCompra = float (input("Digite o valor da sua compra: "))
CupomDesconto = input ("Possui cupom de desconto?: ")

if (ValorCompra >=200 or CupomDesconto == "SIM"):
    print ("Você ganhou um desconto de 15%!")

else:
    print("Você não tem direito a descontos no momento!")