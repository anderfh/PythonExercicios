from random import randint
from time import sleep
from operator import itemgetter
print('\033cValores Sorteados:')
jogo = dict()
for c in range(0, 4):
    jogo[f'jogador {c + 1}'] = randint(1, 6)
for k, v in jogo.items():
    sleep(1)
    print(f'    O {k} tirou {v}')
sleep(2)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
#print(ranking)
print('Ranking dos jogadores:')
cont = 0
for c, d in enumerate(ranking):
    sleep(1)
    print(f'    {c + 1}º lugar: {d[0]} com {d[1]}')
