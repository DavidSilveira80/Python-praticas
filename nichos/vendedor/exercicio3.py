"""
Objetivo Técnico: Combinar lógica de desconto progressivo e validação de dados.

História de Usuário: "Como vendedor, preciso aplicar descontos progressivos com base na quantidade de itens comprados pelo cliente."
Passo a Passo:

Defina regras de desconto (ex.: 5% para 3+ itens, 10% para 5+ itens).
Valide se a entrada do cliente contém apenas números inteiros positivos.
Implemente a lógica para calcular o desconto com base na quantidade de itens.
Exiba o valor final com o desconto aplicado.

Conceitos Necessários: Condicionais aninhadas, operadores lógicos, validação de entrada.

Exemplo I/O:

Entrada: quantidade_itens = 6; valor_unitario = 50
Saída Esperada: Valor Total: R$270 (Desconto de 10%)
"""

def validacao_de_entradas(quantidade, valor):
    if (type(quantidade) == int and quantidade > 0) and (type(valor) == int and valor > 0):
        return True
    else:
        return False

def regrando_desconto_preco_cheio(quantidade):
    if 1 <= quantidade <= 2:
        return True
    else:
        return False

def regrando_desconto_5_por_cento(quantidade):
    if 3 <= quantidade < 5:
        return True
    else:
        return False

def calculando_desconto_5_por_cento(quantidade, valor):
    valor_cheio = quantidade * valor
    return valor_cheio - ((valor_cheio * 5) // 100)

def regrando_desconto_10_por_cento(quantidade):
    if quantidade >= 5:
        return True
    else:
        return False


def calculando_desconto_10_por_cento(quantidade, valor):
    valor_cheio = quantidade * valor
    return valor_cheio - ((valor_cheio * 10) // 100)

if __name__ == "__main__":
    quantidade_produto = 6
    valor_unitario = 50

    if validacao_de_entradas(quantidade_produto, valor_unitario):
        print("Continuando com os cálculos")
        if regrando_desconto_preco_cheio(quantidade_produto):
            print(f"R${(quantidade_produto * valor_unitario)} (Preço Cheio)")

        elif regrando_desconto_5_por_cento(quantidade_produto):
            print("Você terá um desconto de 5%")
            print(f"R${calculando_desconto_5_por_cento(quantidade_produto, valor_unitario)} (Desconto de 5%")

        elif regrando_desconto_10_por_cento(quantidade_produto):
            print(f"R${calculando_desconto_10_por_cento(quantidade_produto, valor_unitario)} (Desconto de 10%)")
    else:
        print("Dados inválidos.")
