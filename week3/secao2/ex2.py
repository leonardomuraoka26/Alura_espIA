'''2. Escreva uma função que gere a tabuada de um número inteiro de 1 a 10,
de acordo com a escolha da pessoa usuária. Como exemplo, para o número 7, a
tabuada deve ser mostrada no seguinte formato:

Tabuada do 7:
7 x 0 = 0
7 x 1 = 7
[...]
7 x 10 = 70
'''

while True:
    numero = (input("Escolha um número de 1 a 10: "))
    try: 
        numero = int(numero)
        if numero < 1 or numero > 10:
            print("O número deve ser entre 1 e 10")
        else:
            break
    except ValueError:
        print(f"{numero} não é um número")

def tabuada(numero: int):
    print(f"Tabuada do {numero}:")

    for i in range(11):
        resultado = i * numero
        print(f"{numero} X {i} = {resultado}")

print(tabuada(numero))