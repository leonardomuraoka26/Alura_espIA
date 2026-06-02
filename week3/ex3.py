lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

def mult_3(lista: list=[0]) -> list:
    multiplos = []
    for i in lista:
        if i % 3 == 0:
            multiplos.append(i)
    return multiplos

print(mult_3(lista))