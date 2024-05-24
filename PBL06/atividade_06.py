# Escreva um programa que crie duas listas, uma com os números pares de 1 a 10 
# e outra com os números ímpares de 1 a 10. Em seguida, junte as duas listas em 
# uma terceira lista e a imprima na tela.

lista_par = []

lista_impar = []

for i in range(1,11):

    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)
    
   

print(lista_par)
print(lista_impar)

juncao_listas = lista_par + lista_impar
juncao_listas.sort()

print(juncao_listas)