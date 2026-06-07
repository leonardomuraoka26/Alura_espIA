'''10. Nessa mesma tabela de cadastro de filiais, há uma coluna com as informações
da quantidade de pessoas colaboradoras e o(a) gestor(a) gostaria de ter um
agrupamento da soma dessas pessoas para cada estado. As informações contidas na tabela são:'''
funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]
'''A partir da lista de tuplas, crie um dicionário em que as chaves são os nomes
dos Estados únicos e os valores são as listas com o número de colaboradores(as)
referentes ao Estado. Crie também um dicionário em que as chaves são os nomes dos Estados
e os valores são a soma de colaboradores(as) por Estado.'''

sp = [item[1] for item in funcionarios if item[0] == 'SP']
es = [item[1] for item in funcionarios if item[0] == 'ES']
mg = [item[1] for item in funcionarios if item[0] == 'MG']
rj = [item[1] for item in funcionarios if item[0] == 'RJ']
lista_de_estados = [sp, es, mg, rj]

coluna = ['SP', 'ES', 'MG', 'RJ']

#Formato {chave: valor for item in lista}
dicionario_1 = {coluna[i]: lista_de_estados[i] for i in range(len(lista_de_estados))}
dicionario_2 = {coluna[i]: sum(lista_de_estados[i]) for i in range(len(lista_de_estados))}

print(dicionario_1)
print(dicionario_2)