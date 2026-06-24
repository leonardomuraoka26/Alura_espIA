'''Para praticar os métodos aprendidos no decorrer dessa aula e também aprender novos,
vamos realizar algumas análises utilizando um arquivo csv diferente: alunos.csv.

1) Importe o arquivo alunos.csv e armazene seu conteúdo em um DataFrame Pandas.

2) Visualize as primeiras 7 linhas do DataFrame e as 5 últimas.

3) Confira a quantidade de linhas e colunas desse DataFrame.

4) Explore as colunas do DataFrame e analise os tipos dos dados presentes em cada coluna.'''

import pandas as pd

#1)
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'
dataframe = pd.read_csv(url)

#2)
print('7 primeiras linhas:')
print(dataframe.head(7))
print()
print('5 últimas linhas:')
print(dataframe.tail(5))
print()

#3)
print('Quantidade de linhas e colunas (linhas, colunas):')
print(dataframe.shape)
print()

#4)
#Explorando as colunas
print('Colunas:')
print(dataframe.columns)
print()
#Vendo os tipos de dados
print('Datatypes:')
print(dataframe.dtypes)