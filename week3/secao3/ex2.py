'''2. Crie um código para gerar uma lista que armazena o terceiro
elemento de cada tupla contida na seguinte lista de tuplas:'''
lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

#Formato [expressão for item in lista]
terceiro = [elemento[2] for elemento in lista_de_tuplas]
print(f"Lista com os terceiros elementos: {terceiro}")