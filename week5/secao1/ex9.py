'''Miguel está desenvolvendo um sistema de cupons de desconto e precisa de
uma forma para aplicar diferentes taxas de desconto sobre os valores das compras.

Diante deste problema, crie uma closure que gere uma função capaz de calcular o
preço final com um desconto fixo definido pelo usuário.'''

def criar_desconto(porcentagem: int):
    def calcular_preco(valor: float):
        return (100 - porcentagem) * valor / 100
    return calcular_preco

desconto = int(input("Digite a porcentagem de desconto: "))
compra = float(input("Digite o valor da compra: "))

criar_preco_final = criar_desconto(desconto)
valor_final = criar_preco_final(compra)

print(f"Preço final com desconto: {valor_final}")