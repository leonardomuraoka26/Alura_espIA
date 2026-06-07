'''8. Como cientista de dados em um time de futebol, você precisa implementar
novas formas de coleta de dados sobre o desempenho de jogadores e do time como um
todo. Sua primeira ação é criar uma forma de calcular a pontuação do time no campeonato
nacional a partir dos dados de gols marcados e sofridos em cada jogo.

Escreva uma função chamada calcula_pontos que recebe como parâmetros duas listas
de números inteiros, representando os gols marcados e sofridos pelo time em cada partida
do campeonato. A função deve retornar a pontuação do time e o aproveitamento em percentual,
levando em consideração que a vitória vale 3 pontos, o empate vale 1 ponto e a derrota 0 pontos.'''

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