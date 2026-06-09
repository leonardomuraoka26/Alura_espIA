'''Mariana é responsável por liberar o acesso ao escritório e precisa de um
programa que verifique se os funcionários podem entrar. Para isso, ela usará o
horário atual. O escritório só permite acesso entre 8h e 18h. Crie um programa que
receba a hora atual como entrada (em formato de 24 horas) e exiba uma mensagem
informando se o acesso é permitido ou negado.'''

while True:
    try:
        horario = input("Digite a hora atual (formato 24 horas): ").strip().lower()
        horas, minutos = horario.split(":")
        horas = int(horas)
        minutos = int(minutos)
    except Exception:
        try:
            horas, minutos = horario.split("h")
            horas = int(horas)
            minutos = int(minutos)
        except Exception:
            print("Informe horas e minutos.")
            continue

    if horas >= 24 or horas < 0 or minutos > 59 or minutos < 0:
        print("Horário inválido.")
    else:
        if horas < 8 or (horas == 18 and minutos > 0) or horas > 18:
            print("Acesso negado.")
        else:
            print("Acesso permitido.")
        break