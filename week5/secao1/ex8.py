'''Joana está participando de um processo seletivo para uma vaga de
desenvolvedora e recebeu um desafio técnico de criar uma calculadora para
somar, subtrair, multiplicar e dividir dois números.

Sua tarefa é criar um programa usando funções lambda que receba dois números
e um operador matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.'''

while True:
    numero1 = input("Digite o primeiro número: ")
    try:
        numero1 = float(numero1)
    except Exception:
        print(f'Erro: "{numero1}" não é um número.')
        continue

    numero2 = input("Digite o segundo número: ")
    try:
        numero2 = float(numero2)
    except Exception:
        print(f'Erro: "{numero2}" não é um número.')
        continue

    operador = input("Escolha a operação(| + | - | * | / |): ").strip().lower()
    if operador != "+" and operador != "-" and operador != "*" and operador != "/":
        if operador == "x":
            print(f'Erro: operação inválida ({operador}). Para multiplicação, utilize "*".')
        elif operador == ":":
            print(f'Erro: operação inválida ({operador}). Para divisão, utilize "/".')
        else:
            print(f"Erro: operação inválida ({operador}).")
        continue

    if operador == "/" and numero2 == 0:
        print("Erro: divisão por zero.")
        continue

    break

soma = lambda x, y: x + y
sub = lambda x, y: x - y
mult = lambda x, y: x * y
div = lambda x, y: x / y

operacoes = {"+": soma,
             "-": sub,
             "*": mult,
             "/": div}

resultado = operacoes[operador](numero1, numero2)
print(f"O resultado é: {resultado}")