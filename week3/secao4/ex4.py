'''4. Crie uma função que recebe duas listas como parâmetros e agrupe os elementos
um a um das listas, formando uma lista de tuplas de 3 elementos, no qual o primeiro e
segundo elemento da tupla são os valores na posição i das listas e o terceiro elemento é
a soma dos valores na posição i das listas.

A função deve conter um tratamento de erro indicando o tipo de erro gerado e
retornar como resultado a lista de tuplas. Caso as listas enviadas como parâmetro
tenham tamanhos diferentes, a função deve retornar um IndexError com a frase:
'A quantidade de elementos em cada lista é diferente.'

Dados para testar a função:'''
lista1 = [4,6,7,9,10]
lista2 = [-4,6,8,7,9]

lista3 = [4,6,7,9,10,4]
lista4 = [-4,6,8,7,9]

lista5 = [4,6,7,9,'A']
lista6 = [-4,'E',8,7,9]

def soma_listas(lista1: list, lista2: list):
    try:
        lista_final = [(lista1[i], lista2[i], lista1[i] + lista2[i]) for i in range(len(lista1))]
    except IndexError:
        return "A quantidade de elementos em cada lista é diferente."
    except TypeError:
        return "As listas devem ser compostas somente por números."
    else:
        return lista_final

final_certo = soma_listas(lista1, lista2)
print(final_certo)

final_index = soma_listas(lista3, lista4)
print(final_index)

final_type = soma_listas(lista5, lista6)
print(final_type)