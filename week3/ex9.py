distancia = {"Salvador": 850,
             "Fortaleza": 800,
             "Natal": 300,
             "Aracaju": 550}

passeio = {"Salvador": 200,
           "Fortaleza": 400,
           "Natal": 250,
           "Aracaju": 300}

gasto_hotel = lambda x: x*150

gasto_gasolina = lambda x: distancia[x] * 5 / 14

gasto_passeio = lambda x, y: passeio[x]*y

while True: 
    cidade = input("Nome da cidade: ").capitalize()
    if cidade not in distancia.keys():
        print("Cidade inválida!")
    else:
        break

while True:
    dias = input("Dias: ")
    try:
        dias = int(dias)
        break
    except ValueError:
        print("Entre uma quantidade válida de dias!")

gasto_total = gasto_hotel(dias) + gasto_gasolina(cidade) + gasto_passeio(cidade, dias)

print(f"Com base nos gastos definidos, uma viagem de {dias} dias para {cidade} saindo de Recife custaria {gasto_total:.2f} reais")