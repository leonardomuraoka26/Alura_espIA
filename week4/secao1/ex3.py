'''Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de
servidores não ultrapasse 25°C. Ele quer um programa que receba a temperatura
atual como entrada e, se necessário, exiba uma mensagem de alerta.'''

while True:
    try:
        temperatura = int(input("Digite a temperatura atual: "))
    except ValueError:
        print("Digite uma temperatura válida")
    else:
        if temperatura > 25:
            print("Alerta! Temperatura acima do limite permitido.")
        else:
            print("Temperatura dentro do limite seguro.")
        break