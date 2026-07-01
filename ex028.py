from random import randint
print(' --- Exercício 28 ---')
print('-- Jogo adivinhação --\n')
n = randint(1, 6)
print('Lançando o dado ...')
num = int(input('Qual o número foi sorteado no dado? '))
if num == n:
    print('Parabéns, você acertou na mosca!')
else:
    print('que pena, mais sorte da próxima vez')
