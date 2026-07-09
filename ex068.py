from cores import cabecalho
from time import sleep
from random import randint
titulo = 'Exercício 68'
subtitulo = 'Par ou Impar?'
cont = 0
while True:
    cabecalho(titulo, subtitulo)
    n = int(input('Digite um número: '))
    while True:
        pi = input('Par ou ímpar? (P/I) ').strip().upper()[0]
        if pi in 'PI':
            break
    ai = randint(1, 11)
    r = (n + ai) % 2
    print(f'Você jogou {n} e o computador {ai}, total de {n + ai} {'PAR' if r == 0 else 'IMPAR'}.')
    if (r == 0 and pi == 'P') or (r == 1 and pi == 'I'):
        cont += 1
        print('Você GANHOU, jogue novamente!')
        sleep(3)
    else:
        print('Você PERDEU.')
        break
print(f'GAME OVER ---- Você teve {cont} vitórias consecutivas.')
