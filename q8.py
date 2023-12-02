# Leitura dos valores
hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input("Digite a hora inicial, minuto inicial, hora final e minuto final separados por espaço: ").split())

# Cálculo da duração do jogo em minutos
horas_totais = hora_final - hora_inicial
minutos_totais = minuto_final - minuto_inicial


if minutos_totais < 0:
    minutos_totais += 60
    horas_totais -= 1

if horas_totais < 0:
    horas_totais += 24

# duração
print(f"O JOGO DUROU {horas_totais} HORA(S) E {minutos_totais} MINUTO(S)")

