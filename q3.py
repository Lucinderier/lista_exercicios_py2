# Definição das tarifas de energia elétrica
tarifa_residencial = 0.40  # Menor ou igual a 500 kWh
tarifa_residencial_excedente = 0.65  # Acima de 500 kWh

tarifa_industrial = 0.55  # Menor ou igual a 1000 kWh
tarifa_industrial_excedente = 0.60  # Acima de 1000 kWh

tarifa_comercial = 0.55  # Menor ou igual a 5000 kWh
tarifa_comercial_excedente = 0.60  # Acima de 5000 kWh

# Leitura dos dados
kWh_consumido = float(input("Digite a quantidade de kWh consumida: "))
tipo_instalacao = input("Digite o tipo de instalação (R - Residências, I - Indústrias, C - Comércios): ")

# Cálculo do preço a pagar
if tipo_instalacao == 'R':
    if kWh_consumido <= 500:
        preco_a_pagar = kWh_consumido * tarifa_residencial
    else:
        preco_a_pagar = kWh_consumido * tarifa_residencial_excedente
elif tipo_instalacao == 'I':
    if kWh_consumido <= 1000:
        preco_a_pagar = kWh_consumido * tarifa_industrial
    else:
        preco_a_pagar = kWh_consumido * tarifa_industrial_excedente
elif tipo_instalacao == 'C':
    if kWh_consumido <= 5000:
        preco_a_pagar = kWh_consumido * tarifa_comercial
    else:
        preco_a_pagar = kWh_consumido * tarifa_comercial_excedente
else:
    print("Tipo de instalação inválido!")
    exit(1)

# Exibição do resultado
print("O preço a pagar pelo fornecimento de energia elétrica é de R$ {:.2f}".format(preco_a_pagar))
