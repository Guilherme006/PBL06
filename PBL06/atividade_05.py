# Escreva um programa que crie uma lista de palavras e imprima a palavra mais 
# longa e a palavra mais curta da lista.

frase = input("Digite uma frase: ")


lista_palavras = frase.split()


palavra_mais_longa = max(lista_palavras, key=len)


palavra_mais_curta = min(lista_palavras, key=len)


print("Palavra mais longa:", palavra_mais_longa)
print("Palavra mais curta:", palavra_mais_curta)