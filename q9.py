import random

while True:
    opcoes = ['pedra', 'papel', 'tesoura']
    
    opcao_computador = random.randint(0, 2)
    opcao_computador = opcoes[opcao_computador]
    
    opcao_jogador = input("Escolha pedra, papel ou tesoura (ou 'sair' para encerrar o jogo): ").lower()
    
    if opcao_jogador == 'sair':
        print("Jogo encerrado.")
        break
    
    if (opcao_computador == 'pedra' and opcao_jogador == 'tesoura') or \
       (opcao_computador == 'tesoura' and opcao_jogador == 'papel') or \
       (opcao_computador == 'papel' and opcao_jogador == 'pedra'):
        print("Jogador venceu!")
    elif opcao_computador == opcao_jogador:
        print("Empate!")
    else:
        print("Computador venceu!")
