def calcula_pontos(gols_marcados, gols_sofridos):
    diferenca_gols = map(lambda x, y: x-y, gols_marcados, gols_sofridos)
    diferenca_gols = list(diferenca_gols)

    pontos = 0
    for i in diferenca_gols:
        if i > 0:
            pontos += 3
        elif i == 0:
            pontos += 1
    
    pontos_maximos = 3 * len(diferenca_gols)
    aproveitamento = (pontos / pontos_maximos) * 100

    return (pontos, aproveitamento)

gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]

pontos, aprov = calcula_pontos(gols_marcados, gols_sofridos)
print(f"A pontuação do time foi de {pontos} e seu aproveitamento foi de {aprov:.0f}%.")