'''Clara está gerenciando o estoque de sua loja e recebeu duas listas separadas:
uma contendo os nomes dos produtos e outras com seus respectivos preços. Para
facilitar a organização, ela precisa combinar essas listas de forma que cada
produto seja associado ao seu preço.

Crie um programa que junte as listas e exiba o resultado no formato produto: preço'''

while True:
    produtos = input("Digite os produtos separados por vírgula: ").strip().split(",")
    precos = input("Digite os preços separados por vírgula: ").strip().split(",")

    if len(produtos) != len(precos):
        print("As listas devem ter o mesmo tamanho.")
        continue
    else:
        for i in range(len(produtos)):
            print(f"{produtos[i].strip()}: {precos[i].strip()}")
        break
        