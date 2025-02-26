
"""
Objetivo Técnico: Praticar manipulação de listas e loops.
História de Usuário: "Como vendedor, preciso listar todos os produtos disponíveis no estoque com
seus preços para apresentar ao cliente."
Passo a Passo:

Identifique quais informações são necessárias para representar um produto (ex.: nome, preço).

Crie uma lista de produtos fictícios com essas informações.

Use um loop para exibir cada produto e seu preço formatado.
Adicione uma condição para destacar produtos com preço acima de R$100.
Conceitos Necessários: Listas, loops (for), formatação de strings, condicionais (if).

Exemplo I/O:

Entrada: produtos = [{"nome": "Camiseta", "preco": 50}, {"nome": "Tênis", "preco": 120}]

Saída Esperada:

Produto: Camiseta | Preço: R$50
Produto: Tênis | Preço: R$120 (Destaque: Produto Premium)


"""

def listagem_de_produtos(lista_produtos):
    for produto in lista_produtos:
        if produto["preco"] > 100.0:
            print(f'Produto: {produto["nome"]} | Preço: R${produto["preco"]:.2f} (Destaque: Produto Premium')
        else:
            print(f'Produto: {produto["nome"]} | Preço: R${produto["preco"]:.2f}')

if __name__ == "__main__":

    produtos = [
        {"nome": "Camiseta", "preco": 50.0},
        {"nome": "Tênis", "preco": 120.0},
        {"nome": "Meia", "preco": 12.0}
    ]

    listagem_de_produtos(produtos)
