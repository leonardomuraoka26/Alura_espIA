'''9. Uma empresa possui filiais espalhadas nos Estados da região Sudeste do Brasil.
Em uma das tabelas de cadastro das filiais há uma coluna contendo a informação de qual
é o Estado a que pertence:'''
estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']

'''A empresa sempre está abrindo novas filiais, de modo que a tabela está constantemente
recebendo novos registros e o gestor gostaria de possuir a informação atualizada da
quantidade de filiais em cada Estado.

A partir da coluna com a informação dos Estados, crie um dicionário
usando dict comprehension com a chave sendo o nome de um Estado e o valor
sendo a contagem de vezes em que o Estado aparece na lista.'''

sp = [item for item in estados if item == 'SP']
es = [item for item in estados if item == 'ES']
mg = [item for item in estados if item == 'MG']
rj = [item for item in estados if item == 'RJ']

lista_de_estados = [sp, es, mg, rj]

coluna = ['SP', 'ES', 'MG', 'RJ']

#Formato {chave: valor for item in lista}
dicionario = {coluna[i]: len(lista_de_estados[i]) for i in range(len(lista_de_estados))}
print(dicionario)