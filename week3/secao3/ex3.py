'''3. A partir da lista:'''
lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']
'''crie um código para gerar uma lista de tuplas em que cada tupla tenha o primeiro elemento
como a posição do nome na lista original e o segundo elemento sendo o próprio nome.'''

lista_de_tuplas = []

for i in range(len(lista)):
    #É preciso adicionar outro parênteses dentro do método append para sinalizar que é uma tupla
    #Caso precise criar uma lista de listas, utiliza-se [] e, um dicionário, {}
    #Isso porque append recebe apenas 1 argumento
    lista_de_tuplas.append((i+1, lista[i]))

print(lista_de_tuplas)