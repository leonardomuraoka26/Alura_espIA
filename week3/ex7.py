nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

nome_completo = map(lambda x, y: x.capitalize() + ' ' + y.capitalize(), nomes, sobrenomes)

for nome in nome_completo:
    print(f"Nome completo: {nome}")