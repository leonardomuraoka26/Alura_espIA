'''Fernanda está planejando uma viagem e quer calcular quanto pagará de pedágio.
O valor do pedágio depende da distância percorrida:

Até 100 km: R$ 10,00
Entre 100 km e 200 km: R$ 20,00
Acima de 200 km: R$ 30,00
Crie um programa que receba a distância percorrida e informe o valor do pedágio correspondente.'''

while True:
    try:
        distancia = input("Digite a distância percorrida (em km): ")
        distancia = float(distancia)
        break
    except Exception:
        try:
            distancia = distancia.replace(",", ".")
            distancia = float(distancia)
            break
        except Exception:
            print("Digite uma distância válida.")
            continue
    
if distancia < 100:
    pedagio = 10
elif distancia >= 300:
    padagio = 30
else:
    pedagio = 20

print(f"Valor do pedágio: R${pedagio},00")