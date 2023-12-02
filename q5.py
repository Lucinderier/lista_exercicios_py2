# Dicionário para mapear números de meses para seus respectivos nomes
meses = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}

# Leitura do valor do usuário
valor = int(input("Digite um valor de 1 a 12: "))

# Verificação e exibição do mês correspondente
if valor in meses:
    nome_mes = meses[valor]
    print(nome_mes)
else:
    print("Valor inválido. Por favor, digite um número de 1 a 12.")
