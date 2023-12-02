# Definição dos preços por km
preco_por_km_ate_200 = 0.50
preco_por_km_acima_200 = 0.45

# Leitura dos dados
distancia_em_km = float(input("Digite a distância em km que deseja percorrer: "))

# Cálculo do preço da passagem
if distancia_em_km <= 200:
    preco_da_passagem = distancia_em_km * preco_por_km_ate_200
else:
    preco_da_passagem = distancia_em_km * preco_por_km_acima_200

# Exibição do resultado
print("O preço da passagem é de R$ {:.2f}".format(preco_da_passagem))
