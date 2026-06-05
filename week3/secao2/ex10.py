frase = input("Frase: ").replace(",", " ").replace(".", " ").replace("!", " ").replace("?", " ").strip()

lista = frase.split()

lista_filtrada = filter(lambda x: len(x) >= 5, lista)
print(list(lista_filtrada))