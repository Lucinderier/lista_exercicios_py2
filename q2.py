salario = float(input("Digite o salário do funcionário: "))

if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

print("O valor do aumento é: ", aumento)

salario_final = salario + aumento

print("O salário final do funcionário é: ", salario_final)