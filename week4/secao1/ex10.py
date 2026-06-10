'''Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:

O valor da renda mensal precisa ser maior que R$ 2.000,00.
O valor da parcela não pode ultrapassar 30% da renda.

Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada.
O programa deve informar se o empréstimo foi aprovado ou negado com base nas condições acima.'''

while True:
    renda = input("Digite o valor da sua renda mensal: ")
    parcela = input("Digite o valor da parcela desejada: ")
    try:
        renda = float(renda)
        parcela = float(parcela)
    except Exception:
        try:
            renda = renda.replace(",", ".")
            renda = float(renda)
            parcela = parcela.replace(",", ".")
            parcela = float(parcela)
        except Exception:
            print("Valor inválido.")
            continue

    porcentagem = parcela / renda
    if parcela > renda:
        print(f"Empréstimo negado: parcela maior do que a renda (Parcela: R${parcela:.2f} X Renda: {renda:.2f}).")
    elif renda < 2000:
        print(f"Empréstimo negado: renda abaixo de R$ 2000 (R$ {renda:.2f}).")
    elif porcentagem > 0.3:
        print(f"Empréstimo negado: parcela acima de 30% da renda ({(porcentagem * 100):.0f}%).")
    else:
        print("Empréstimo aprovado.")
    break