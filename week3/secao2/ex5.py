notas = []

for i in range(5):
    while True:
        nota = input("Nota: ")
        try:
            nota = int(nota)
            break
        except ValueError:
            print("Nota inválida!")
    notas.append(nota)

def media(lista: list) -> float:
    notas.remove(max(lista))
    notas.remove(min(lista))

    nota_final = sum(notas) / len(notas)
    return nota_final

nota = media(notas)
print(f"Nota da manobra: {nota:.2f}")