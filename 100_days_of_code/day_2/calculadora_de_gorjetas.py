print('Bem-vindo a sua Calculadora de Gorjetas.')
valor_total = float(input('Qual foi o valor total? R$ '))
porcentagem = input('Quantos % vocês vão deixar de gorjeta? 10, 12 ou 15? ')
rachadores_de_conta = int(input('Quantos irão rachar a conta? '))
valor_total_mais_gorjeta = 0.0
valor_do_rachuncho = 0.0

if porcentagem == '10':
   valor_total_mais_gorjeta = valor_total + ((valor_total * 10) / 100)
   valor_do_rachuncho = valor_total_mais_gorjeta / rachadores_de_conta
   print(f'Cada Pessoa pagará: R$ {valor_do_rachuncho:.2f}')
elif porcentagem == '12':
   valor_total_mais_gorjeta = valor_total + ((valor_total * 12) / 100)
   valor_do_rachuncho = valor_total_mais_gorjeta / rachadores_de_conta
   print(f'Cada Pessoa pagará: R$ {valor_do_rachuncho:.2f}')
if porcentagem == '15':
   valor_total_mais_gorjeta = valor_total + ((valor_total * 15) / 100)
   valor_do_rachuncho = valor_total_mais_gorjeta / rachadores_de_conta
   print(f'Cada Pessoa pagará: R$ {valor_do_rachuncho:.2f}')
