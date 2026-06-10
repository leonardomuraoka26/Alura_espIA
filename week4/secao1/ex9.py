'''Lucas está desenvolvendo um jogo e precisa de uma funcionalidade que verifique
se um número é par ou ímpar. Essa verificação será usada para definir ações
diferentes dentro do jogo. Escreva um programa que receba um número inteiro e exiba
uma mensagem informando se ele é par ou ímpar.'''

while True:
    numero = input("Digite um número inteiro: ")
    try:
        numero = int(numero)
    except Exception:
        print(f"{numero} não é um número inteiro. Digite novamente.")
    else:
        if numero % 2 == 0:
            paridade = "par"
        else:
            paridade = "ímpar"
        print("O número é " + paridade)
        break