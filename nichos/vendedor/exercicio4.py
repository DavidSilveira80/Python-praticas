"""
Objetivo Técnico: Praticar modularização e reutilização de código.
História de Usuário: "Como vendedor, preciso gerar relatórios de vendas diárias agrupando produtos por categoria."
Passo a Passo:

Crie uma estrutura para representar produtos com categorias (ex.: Eletrônicos, Vestuário).
Escreva uma função que agrupe produtos por categoria.
Implemente outra função para calcular o total vendido por categoria.
Exiba um relatório organizado com os totais.
Conceitos Necessários: Modularização, dicionários aninhados, funções reutilizáveis.
Exemplo I/O:
Entrada:

vendas = [
    {"categoria": "Eletrônicos", "valor": 500},
    {"categoria": "Vestuário", "valor": 200},
    {"categoria": "Eletrônicos", "valor": 300}
]

Saída Esperada:

Relatório de Vendas:
- Eletrônicos: R$800
- Vestuário: R$200
"""

def verfica_se_categoria_esta_no_total_de_categorias(tot_categorias, categoria):
    if categoria not in tot_categorias:
        return False
    else:
        return True

def gerar_dicionario_do_valor_total_de_cada_categoria_vendida(categorias_vendidas):
    total_das_categorias = {}
    for categoria in categorias_vendidas:
        if verfica_se_categoria_esta_no_total_de_categorias(total_das_categorias, categoria["categoria"]):
            total_das_categorias[categoria["categoria"]] += categoria["valor"]
        else:
            total_das_categorias[categoria["categoria"]] = categoria["valor"]
    return total_das_categorias

def gera_relatorio_de_venda(categorias_vendidas):

    for k,v in categorias_vendidas.items():
        print(f"- {k}: R$ {v}")

if __name__ == "__main__":
    vendas = [
        {"categoria": "Eletrônicos", "valor": 500},
        {"categoria": "Vestuário", "valor": 200},
        {"categoria": "Eletrônicos", "valor": 300},
        {"categoria": "Alimentos", "valor": 150},
        {"categoria": "Cosméticos", "valor": 120},
        {"categoria": "Vestuário", "valor": 400},
        {"categoria": "Eletrônicos", "valor": 800},
        {"categoria": "Alimentos", "valor": 100},
        {"categoria": "Cosméticos", "valor": 250},
        {"categoria": "Vestuário", "valor": 150}
    ]
    total_vendas = gerar_dicionario_do_valor_total_de_cada_categoria_vendida(vendas)
    print(" Relatório de Vendas:")
    gera_relatorio_de_venda(total_vendas)
