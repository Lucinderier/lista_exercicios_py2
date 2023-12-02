import random

while True:
    numero_secreto = random.randint(1, 100)
    palpite = 0
    
    while palpite != numero_secreto:
        palpite = int(input("Tente adivinhar o número secreto entre 1 e 100 (ou digite 0 para sair): "))
        
        if palpite == 0:
            print("Jogo encerrado.")
            exit()
        elif palpite > numero_secreto:
            print("Tente um número menor.")
        elif palpite < numero_secreto:
            print("Tente um número maior.")
    
    print(f"Parabéns! Você acertou o número secreto: {numero_secreto}")
