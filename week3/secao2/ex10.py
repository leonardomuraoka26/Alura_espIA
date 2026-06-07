'''10. Você iniciou um estágio em uma empresa que trabalha com processamento
de linguagem natural (NLP). Sua líder requisitou que você criasse um trecho de
código que recebe uma frase digitada pela pessoa usuária e filtre apenas as
palavras com tamanho maior ou igual a 5, exibindo-as em uma lista. Essa demanda
é voltada para a análise do padrão de comportamento de pessoas na escrita de
palavras acima dessa quantidade de caracteres.'''

frase = input("Frase: ").replace(",", " ").replace(".", " ").replace("!", " ").replace("?", " ").strip()

lista = frase.split()

lista_filtrada = filter(lambda x: len(x) >= 5, lista)
print(list(lista_filtrada))