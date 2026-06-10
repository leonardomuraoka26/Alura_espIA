'''Uma professora precisa de um programa que ajude a calcular a média final dos
alunos e informe se foram aprovados, ficaram de recuperação ou reprovados. As regras são:

Média >= 7: Aprovado
5 <= Média < 7: Recuperação
Média < 5: Reprovado

Escreva um programa que receba três notas como entrada e calcule a média final.
Com base na média, exiba a situação do aluno.'''

while True:
    nota1 = input("Digite a primeira nota: ")
    nota2 = input("Digite a segunda nota: ")
    nota3 = input("Digite a terceira nota: ")
    try:
        nota1 = float(nota1)
        nota2 = float(nota2)
        nota3 = float(nota3)
    except Exception as e:
        try:
            nota1 = nota1.replace(",", ".")
            nota1 = float(nota1)
            nota2 = nota2.replace(",", ".")
            nota2 = float(nota2)
            nota3 = nota3.replace(",", ".")
            nota3 = float(nota3)
        except Exception as e:
            print("Nota inválida")
            continue

    media = (nota1 + nota2 + nota3) / 3
    print(f"Média: {media:.2f}")
    if media >= 7:
        print("Aprovado(a)")
    elif media >= 5:
        print("Recuperação")
    else:
        print("Reprovado(a)")
    break