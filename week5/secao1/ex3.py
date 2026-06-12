'''Beatriz está desenvolvendo um sistema de atendimento para um site de serviços.
Ela deseja criar um programa que exiba uma saudação personalizada dependendo da hora
do dia que o usuário acessa a plataforma. O sistema deverá ter a seguinte regra:

Se for antes das 12h, exibir "Bom dia";

Entre 12h e 18h, exibir "Boa tarde";

Após 18h, exibir "Boa noite".'''

def saudacao(hora: int) -> str:
    if hora < 12:
        return "Bom dia!"
    elif hora <= 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"
    
while True:
    hora = input("Digite a hora atual (0-23): ")
    try:
        hora = int(hora)
    except Exception:
        print(f"Hora inválida: {hora}")
    else:
        if hora < 0 or hora > 23:
            print(f"Hora inválida: {hora}")
        else:
            print(saudacao(hora))
            break