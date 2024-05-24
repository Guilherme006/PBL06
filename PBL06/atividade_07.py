# Escreva um programa que crie uma lista com os números de 1 a 100. Em seguida, 
# imprima apenas os números pares da lista.

numeros_pares = []

for i in range(1,101):

    if i % 2 == 0:
        numeros_pares.append(i)

print(numeros_pares)
