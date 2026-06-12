'''Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia.
As vendas são informadas em uma única linha separadas por espaços.

Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total.'''

def soma_vendas(linha: str) -> float:
    lista = linha.split()
    soma = sum(map(float, lista))
    return soma

valores = input("Digite os valores das vendas: ")
print(f"O total de vendas foi: {soma_vendas(valores)}")