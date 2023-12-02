# Leitura dos valores
A, B, C, D = map(int, input("Digite quatro valores inteiros A, B, C e D separados por espaço: ").split())

# Verificação das condições
if (B > C) and (D > A) and (C + D > A + B) and (C > 0) and (D > 0) and (A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores não aceitos")
