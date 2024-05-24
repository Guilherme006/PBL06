# Escreva um programa que crie uma lista com as letras do alfabeto e embaralhe 
# suas posições. Em seguida, peça ao usuário para adivinhar a posição correta de 
# uma determinada letra e informe se ele acertou ou errou.


import random


alfabeto = list('abcdefghijklmnopqrstuvwxyz')


random.shuffle(alfabeto)


# print("Lista embaralhada:", alfabeto)


letra = input("Digite uma letra para adivinhar a posição: ").lower()


posicao_adivinhada = int(input(f"Qual é a posição correta da letra '{letra}' na lista embaralhada? (0 a 25): "))


if alfabeto[posicao_adivinhada] == letra:
    print("Parabéns! Você acertou.")
else:
    print(f"Você errou. A letra '{letra}' está na posição {alfabeto.index(letra)}.")


print("Posição correta da letra na lista embaralhada:", alfabeto.index(letra))
