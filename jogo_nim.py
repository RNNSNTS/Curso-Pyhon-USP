#cr = computador remove
#jr = jogador remove
# jval = Jogada Valida
# computer = vez do computador jogar



def computador_escolhe_jogada(n, m):
    cr = 1

    while cr != m:
        if (n - cr) % (m+1) == 0:
            return cr

        else:
            cr += 1

    return cr


def usuario_escolhe_jogada(n, m):
    jval = False

    while not jval:
        jr = int(input('Quantas peças você vai tirar? '))
        if jr > m or jr< 1:
            print('Oops! Jogada inválida! Tente de novo.')
            print()

        else:
            jval= True

    return jr


def campeonato():
    Rodada = 1
    while Rodada <= 3:
        print()
        print('**** Rodada', Rodada, '****')
        print()
        partida()
        Rodada += 1
    print()
    print('Placar: Você 0 X 3 Computador')


def partida():
    n = int(input('Quantas peças? '))

    m = int(input('Limite de peças por jogada? '))

    computer = False

    if n % (m+1) == 0:
        print()
        print('Voce começa!')

    else:
        print()
        print('Computador começa!')
        computer = True

    while n > 0:
        if computer:
            cr = computador_escolhe_jogada(n, m)
            n = n - cr
            if cr == 1:
                print()
                print('O computador tirou uma peça')
            else:
                print()
                print('O computador tirou', cr, 'peças')

            computer = False
        else:
            jr = usuario_escolhe_jogada(n, m)
            n = n - jr
            if jr == 1:
                print()
                print('Você tirou uma peça')
            else:
                print()
                print('Você tirou', jr, 'peças')
            computer = True
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
            print()
        else:
            if n != 0:
                print('Agora restam,', n, 'peças no tabuleiro.')
                print()

    print('Fim do jogo! O computador ganhou!')

# Incio
print('Bem-vindo ao jogo do NIM! Escolha:')
print()

print('1 - para jogar uma partida isolada')
print ('2 - para jogar um campeonato ')

tipoDePartida = int(input())

if tipoDePartida == 2:
    print()
    print('Voce escolheu um campeonato!')
    print()
    campeonato()
else:
    if tipoDePartida == 1:
        print()
        partida()



    
