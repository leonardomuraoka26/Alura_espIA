'''4. Crie uma lista usando o list comprehension que
armazena somente o valor numérico de cada tupla caso o primeiro
elemento seja 'Apartamento', a partir da seguinte lista de tuplas:'''
aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

#Formato [expressão for item in lista if condição]
#Caso use um else, usa-se o formato [resultado_if if cond else resultado_else for item in lista]
lista = [tupla[1] for tupla in aluguel if tupla[0] == 'Apartamento']
print(lista)