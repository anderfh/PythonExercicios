from cores import cabsub
from time import sleep
from random import randint
linha = '.$.¢'
sub = 'Gerador de jogos - Mega Sena'
cabsub(sub, linha)
n = int(input('Quantos jogos gostaria de gerar? '))
print(f'{'Sorteando . . .':^30}')
sleep(2)
lista = list()
jogo = list()
for c in range(0, n):
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
        if len(jogo) == 6:
            break
    lista.append(jogo[:])
    jogo.clear()    
for c in range(0, len(lista)):
    lista[c].sort()
    print(f'Jogo {c + 1}:', end='')
    for j in range(0, len(lista[c])):
        print(f' {lista[c][j]:>2}', end='')
        if j < len(lista[c]) - 2:
            print(',', end='')
        elif j < len(lista[c]) - 1:
            print(' e', end='')
        else:
            print('.')
    sleep(1)
print('----------> Boa Sorte ! <-----------')
