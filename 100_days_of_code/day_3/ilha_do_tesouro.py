print('Bem-vindo, você está na Ilha Do Tesouro')
print('Sua Missão é encontrar o cobiçado Tesouro')
print('Porém muito cuidado com os perigos e armadilhas deste lugar.')

inicio = input('Você está em uma encruzilhada você quer ir pela esquerda ou direita? (esquerda/direita)  ')
if inicio == 'direita':
    print('Você caiu em um buraco com lanças envenenadas. Fim de Jogo')
elif inicio == 'esquerda':
    nadar_ou_esperar = input('Indo pela trilha esquerda ao final você chegou á um lago. Você prefere atravessar o '
                              'lago à nado\n'
          'ou prefere esperar e observar mais o cenário? (nadar/esperar) ')
    if nadar_ou_esperar == 'nadar':
        print('Você foi atacado e devorado por Trutas assassinas. Fim de Jogo.')
    elif nadar_ou_esperar == 'esperar':
        porta = input('Ao observar melhor à sua volta você encontra encrustradas em uma grande Rocha três Portas: \n'
                      'Uma vermelha, uma Azul e outra Amarela.É certo que em uma delas o Tesouro da ilha está escondido.\n'
                      'Qual delas você vai abrir? (vermelha/azul/amarela) ')
        if porta == 'vermelha':
            print('Você foi devorado por uma grande bola de fogo. Fim de Jogo.')
        elif porta == 'azul':
            print('Você foi devorado por uma prole de Bestas Famintas. Fim de Jogo.')
        else:
            print("Ao abrir a porta Amarela você encontra sobre uma mesa de pedra um rolo de papiro contendo todo o mapeamento\n"
                  "da Ilha com a marcação de todas as armadilhas e como desativa-las, além da localização exata do tão cobiçado\n"
                  "Tesouro. Você seguiu á risca as orientações e encontrou o Tesouro. Parabéns.")

#TODO requer melhorias