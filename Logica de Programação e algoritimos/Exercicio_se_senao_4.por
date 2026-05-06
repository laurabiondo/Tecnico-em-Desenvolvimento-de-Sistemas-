programa {
  funcao inicio() {
    inteiro lado1, lado2,lado3

    escreva ("Digite Lado 1:")
    leia (lado1)

    escreva ("Digite Lado 2:")
    leia (lado2)

    escreva ("Digite Lado 3:")
    leia (lado3)

    se (lado1==lado2 e lado1==lado3 e lado2==lado3){
      escreva ("Triângulo equilátero")
    }

    senao se (lado1==lado2 ou lado1==lado3 ou lado3==lado2){
      escreva ("Triângulo isósceles")
    }

    senao se (lado1!=lado2 e lado1 !=lado3 e lado2!=lado3){
      escreva ("Triângulo escaleno")
    }
    }
  }
}
