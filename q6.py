# Leitura dos valores
A, B, C = map(float, input("Digite três valores de ponto flutuante A, B e C separados por espaço: ").split())

# Ordenação em ordem decrescente
maior = max(A, B, C)
menor = min(A, B, C)
meio = (A + B + C) - maior - menor

# Verificação do tipo de triângulo
if maior >= meio + menor:
    print("Estes valores não formam um triângulo.")
else:
    if maior ** 2 == meio ** 2 + menor ** 2:
        print("Triângulo retângulo.")
    elif maior ** 2 > meio ** 2 + menor ** 2:
        print("Triângulo obtusângulo.")
    else:
        print("Triângulo acutângulo.")

    if A == B == C:
        print("Triângulo equilátero.")
    elif A == B or A == C or B == C:
        print("Triângulo isósceles.")
    else:
        print("Triângulo escaleno.")

