posicao_inicial = float (input("Digite sua posição inicial: "))
posicao_final = float (input("Digite sua posição final: "))
tempo_inicial = float (input("Digite seu tempo inicial: "))
tempo_final = float (input("Digite seu tempo final: "))

vm = (posicao_inicial-posicao_final)/(tempo_final-tempo_inicial)
print ("A velocidade média é:", vm )