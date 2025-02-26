

"""
Objetivo Técnico: Trabalhar com dicionários e funções simples.

História de Usuário: "Como vendedor, preciso calcular o valor total de uma compra com base
nos produtos selecionados pelo cliente."

Passo a Passo:

Crie um dicionário que mapeie os produtos aos seus respectivos preços.
Escreva uma função que receba uma lista de produtos e retorne o valor total da compra.
Valide se todos os produtos estão presentes no dicionário antes de calcular.
Retorne uma mensagem de erro caso algum produto não esteja disponível.

Conceitos Necessários: Dicionários, funções, tratamento de erros (try/except ou condicionais).

Exemplo I/O:

Entrada: estoque = {"Camiseta": 50, "Tênis": 120}; compra = ["Camiseta", "Tênis"]
Saída Esperada: Valor Total: R$170

"""

def verifica_se_ha_produtos_em_estoque(lista_compras, estoque_de_produtos):

    for produto in lista_compras:
        if produto not in estoque_de_produtos:
            return False
    return True

def calcula_valor_total_da_compra(lista_compras, estoque_de_produtos):
    soma = 0.0
    for produto in lista_compras:
        if produto in estoque_de_produtos:
            soma += estoque_de_produtos[produto]
    return soma

if __name__ == "__main__":

    compra = ["Camiseta", "Tênis", "Bermuda"]

    estoque = {
        "Camiseta": 135,
        "Tênis": 128,
        "Jaqueta": 103,
        "Calça": 159,
        "Chapéu": 169,
        "Bolsa": 87,
        "Bermuda": 90,
        "Tênis de corrida": 74,
        "Moletom": 136,
        "Óculos": 129
    }

    if not verifica_se_ha_produtos_em_estoque(compra, estoque):
        print('Pelo menos um dos produtos não consta no estoque')
    else:
        print("Os produtos desejados constam no estoque.")
        print(f'Valor Total: R$ {calcula_valor_total_da_compra(compra, estoque):.2f}')
