'''5. Como desafio, você recebeu a tarefa de desenvolver um código que contabiliza as
pontuações de estudantes de uma instituição de ensino de acordo com suas respostas num teste.
Este código deve ser testado para um exemplo de 3 estudantes com uma lista de listas em que
cada lista possui as respostas de 5 questões objetivas de cada estudante. Cada questão
vale um ponto e as alternativas possíveis são A, B, C ou D.

Caso alguma alternativa em um dos testes não esteja entre as alternativas possíveis,
você deve lançar um ValueError com a mensagem "A alternativa [alternativa] não é uma opção
de alternativa válida". O cálculo das 3 notas só será realizado mediante as entradas com
as alternativas A, B, C ou D em todos os testes. Se não for lançada a exceção, será exibida
uma lista com as notas em cada teste.

Os dados para o teste do código são:'''
gabarito = ['D', 'A', 'B', 'C', 'A']

def notas(lista: list):
    lista_retornada = []

    for i in range(len(lista)):
        nota = 0
        for j in range(len(lista[i])):
            if lista[i][j] not in ['A', 'B', 'C', 'D']:
                raise ValueError(f"A alternativa {lista[i][j]} não é uma opção válida.")
            if lista[i][j] == gabarito[j]:
                nota += 1
        lista_retornada.append(nota)
    
    return lista_retornada

testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

notasf = notas(testes_sem_ex)
print(notasf)

notasf2 = notas(testes_com_ex)
print(notasf2)