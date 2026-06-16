'''Lucas está desenvolvendo um sistema para gerar relatórios financeiros e precisa
filtrar apenas os valores pares de uma lista de números informada pelo usuário.

Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter().'''

numeros = input("Digite os números separados por espaço: ").strip()

lista = numeros.split()
lista = [int(item) for item in lista]
#É mais prático usar um list comprehension com if, mas o ex pede para usar a função filter()
#lista = [int(item) for item in lista if int(item) % 2 == 0]
pares = list(filter(lambda x: x % 2 == 0, lista))

string = ""
for par in pares:
    string = string + " " + str(par)

print(f"Números pares:{string}")

'''Solução sugerida:

numeros = input("Digite os números separados por espaço: ").split() 
pares = filter(lambda x: int(x) % 2 == 0, numeros) 
print("Números pares:", " ".join(pares))

"spearador".join(lista) pega todos os itens de uma lista e os junta em uma string,
utilizando o separador fornecido como separador
'''