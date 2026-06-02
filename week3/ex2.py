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