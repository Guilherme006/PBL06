# Escreva um programa que peça ao usuário uma frase e converta cada palavra 
# em uma lista separada. Imprima a lista na tela.


# Inserindo cada palavra em uma única lista
frase = input("Digite uma frase: ")


lista_palavras = frase.split()


print("Lista de palavras:", lista_palavras)


# Inserindo cada palavra em uma lista diferente
frase_02 = input("\nDigite uma frase: ")

palavras_02 = frase_02.split()

listas_de_palavras_02 = [[palavra] for palavra in palavras_02]

print("Lista de listas de palavras:", listas_de_palavras_02)

