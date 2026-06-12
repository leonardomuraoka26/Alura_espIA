'''Pedro está criando um sistema de cadastro de produtos para sua loja e percebeu que
todos os números de telefone dos clientes estão armazenados como strings. No entanto,
para facilitar buscas e validações, ele precisa que esses números sejam tratados como inteiros.

Dado o seguinte código com uma lista de números de telefone armazenados incorretamente
como str, faça duas funções, uma que converte os tipos para inteiro e outra que verifica
se a conversão foi feita corretamente e todos os números de telefone são inteiros:'''

telefones = ["(11)98765-4321", "(21)91234-5678", "(31)98765-4321", "(11)91122-3344"]

def int_covert(lista: list) -> list:
    int_list = []
    for item in lista:
        item = item.replace("(", "").replace(")", "").replace("-", "")
        item = int(item)
        int_list.append(item)

    return int_list

def conversao(lista: list) -> str:
    conferir = list(map(lambda x: type(x), lista))
    contador = 0

    for item in conferir:
        if item == int:
            contador += 1

    if contador == len(lista):
        return "Todos os números foram convertidos corretamente!"
    else:
        return "Erro na conversão."

print(conversao(int_covert(telefones)))