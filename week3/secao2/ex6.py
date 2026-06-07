'''6. Para atender a uma demanda de uma instituição de ensino para a análise do
desempenho de seus(suas) estudantes, você precisa criar uma função que receba uma
lista de 4 notas e retorne:

maior nota
menor nota
média
situação (Aprovado(a) ou Reprovado(a))'''

def boletim(lista):

    maior = max(lista)
    menor = min(lista)
    media = sum(lista) / len(lista)

    if media >= 6:
        situacao = "aprovado(a)"
    else:
        situacao = "reprovado(a)"

    return (maior, menor, media, situacao)

lista = []

for _ in range(4):
    while True:
        nota = input("Nota: ")
        try:
            nota = float(nota)
            break
        except ValueError:
            print("Entre uma nota válida")
    lista.append(nota)

maior, menor, media, situacao = boletim(lista)

print(f"O(a) estudante obteve uma média de {media}, com a sua maior nota de {maior} pontos e a menor nota de {menor} pontos e foi {situacao}.")