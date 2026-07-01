from random import randint
from time import sleep
print(' --- Exercício 28 ---')
print('-- Jogo adivinhação --\n')
n = randint(0, 5) # Gera um número aleatório.
print('Estou pensando em um número de 0 a 5 ...')
num = int(input('Em qual número estou pensando? ')) # Usuário entra número.
sleep(3)
if num == n:
    print('Parabéns, você acertou na mosca!')
else:
    print('Que pena era {}, mais sorte da próxima vez'.format(n))
