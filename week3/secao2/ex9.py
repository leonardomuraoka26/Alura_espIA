'''9. Você recebeu o desafio de criar um código que calcula os gastos de
uma viagem para um das quatro cidades partindo de Recife, sendo elas:
Salvador, Fortaleza, Natal e Aracaju.

O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina
na viagem de carro é de 14 km/l, sendo que o valor da gasolina é de 5 reais o litro.
O gastos com passeios e alimentação a se fazer em cada uma delas por dia seria de
[200, 400, 250, 300], respectivamente.

Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente
[850, 800, 300, 550] km, crie três funções nas quais: a 1ª função calcule
os gastos com hotel (gasto_hotel), a 2ª calcule os gastos com a gasolina (gasto_gasolina)
e a 3ª os gastos com passeio e alimentação (gasto_passeio).

Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife.
Considere a viagem de ida e volta de carro.'''

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