import random
pedra_papel_tesoura = ['pedra', 'papel', 'tesoura']
minha_jogada = input('(pedra/papel/tesoura) ')
cpu_jogada = random.choice(pedra_papel_tesoura)

if minha_jogada == 'pedra':
    if cpu_jogada == 'tesoura':
        print('Você venceu.')
    elif cpu_jogada == 'papel':
        print('Você perdeu.')
    elif cpu_jogada == minha_jogada:
        print('Empate')
elif minha_jogada == 'tesoura':
    if cpu_jogada == 'papel':
        print('Você Venceu.')
    elif cpu_jogada == 'pedra':
        print('Você perdeu.')
    elif cpu_jogada == minha_jogada:
        print('Empate')
elif minha_jogada == 'papel':
    if cpu_jogada == 'pedra':
        print('Vocẽ venceu.')
    elif cpu_jogada == 'tesoura':
        print('Você perdeu.')
    elif cpu_jogada == minha_jogada:
        print('Empate.')
# TODO pode precisar de melhorias