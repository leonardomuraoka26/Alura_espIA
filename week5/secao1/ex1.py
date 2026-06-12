'''Julia é professora e precisa de um programa para ajudar seus alunos a calcularem
suas idades com base no ano de nascimento. Sua tarefa é criar uma função que receba
o ano de nascimento e o ano atual e retorne à idade correspondente.'''

def calcula_idade(ano_nascimento: int, ano_atual: int) -> int:
    return ano_atual - ano_nascimento

while True:
    nascimento = input("Digite o ano de nascimento: ")
    atual = input("Digite o ano atual: ")
    try:
        nascimento = int(nascimento)
        atual = int(atual)
    except Exception:
        print("Entre um ano válido.")
        
    else:
        idade = calcula_idade(nascimento, atual)
        if idade < 0:
            print(f"Sua idade não pode ser negativa: {idade}.")
            
        else:
            print(f"A idade é {idade} anos.")
            break