# Se você terminou os exercícios acima. Tente agora fazer o jogo da velha, mas 
# utilizando listas ao invés de vetores.


import random

# Cria um tabuleiro vazio
tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]

# Embaralha o tabuleiro para a simulação de uma situação inicial
random.shuffle(tabuleiro)

# Variável para controlar o jogador atual
jogador_atual = 'X'

# Loop principal do jogo
while True:
    # Imprime o tabuleiro
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 5)
    
    # Solicita ao jogador atual para fazer uma jogada
    print(f"Jogador {jogador_atual}, é sua vez.")
    linha = int(input("Digite a linha (0, 1, 2): "))
    coluna = int(input("Digite a coluna (0, 1, 2): "))

    # Verifica se a posição está ocupada
    if tabuleiro[linha][coluna] != ' ':
        print("Espaço já ocupado. Tente novamente.")
        continue

    # Atualiza o tabuleiro com a jogada do jogador atual
    tabuleiro[linha][coluna] = jogador_atual

    # Verifica condição de vitória
    vitoria = False
    for i in range(3):
        # Verifica linhas e colunas
        if all(tabuleiro[i][j] == jogador_atual for j in range(3)) or \
           all(tabuleiro[j][i] == jogador_atual for j in range(3)):
            vitoria = True
            break
    # Verifica diagonais
    if all(tabuleiro[i][i] == jogador_atual for i in range(3)) or \
       all(tabuleiro[i][2 - i] == jogador_atual for i in range(3)):
        vitoria = True

    if vitoria:
        for linha in tabuleiro:
            print('|'.join(linha))
            print('-' * 5)
        print(f"Parabéns, jogador {jogador_atual}! Você venceu!")
        break

    # Verifica condição de empate
    empate = all(espaco != ' ' for linha in tabuleiro for espaco in linha)
    if empate:
        for linha in tabuleiro:
            print('|'.join(linha))
            print('-' * 5)
        print("O jogo empatou!")
        break

    # Alterna para o próximo jogador
    jogador_atual = 'O' if jogador_atual == 'X' else 'X'
