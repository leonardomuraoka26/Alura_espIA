'''7. Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes
de cada estudante concatenando-as para apresentar seus nomes completos na forma
Nome Sobrenome. As listas são:'''
nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

nome_completo = map(lambda x, y: x.capitalize() + ' ' + y.capitalize(), nomes, sobrenomes)

for nome in nome_completo:
    print(f"Nome completo: {nome}")