from cores import cabecalho
from time import sleep
from random import randint
titulo = 'Exercício 45'
subtitulo = 'JoKenPo'
cabecalho(titulo, subtitulo)
print('''   Opções:
      [ 1 ] P e d r a
      [ 2 ] T e s o u r a
      [ 3 ] P a p e l ''')
mao = (int(input('Qual a sua jogada? ')))-1
pc = randint(0, 2)
res = 'empata com'
if 0<= mao <3:
    if mao == 0:
        if pc == 1:
            res = 'ganha de'
        elif pc == 2:
            res = 'perde de'
    elif mao == 1:
        if pc == 0:
            res = 'perde de'
        elif pc == 2:
            res = 'ganha de'
    elif mao == 2:
        if pc == 0:
            res = 'ganha de'
        elif pc == 1:
            res = 'perde de'
    itens = ('Pedra', 'Tesoura', 'Papel')
    maoRes = itens[mao]
    pcRes = itens[pc]
    print('Jo')
    sleep(1)
    print('Ken')
    sleep(1)
    print('Po!')
    print('{} {} {}'.format(maoRes, res, pcRes))
else:
    print('Jogada inválida !')