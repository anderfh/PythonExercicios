from random import randint
from time import sleep
print('\033cValores Sorteados:')
jogo = dict()
cont = 0
for c in range(0, 4):
    jogo[f'jogador {c + 1}'] = randint(1, 6)
for k, v in jogo.items():
    sleep(1)
    print(f'    O {k} tirou {v}')
sleep(2)
print('Ranking dos jogadores:')
for c in range(6, 1, -1):
    for k, v in jogo.items():
        if v == c:
            cont += 1
            sleep(1)
            print(f'    {cont}º lugar: {k} com {v}')
