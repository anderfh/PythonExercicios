from cores import cabecalho
from random import randint
from time import sleep
titulo = 'Exercício 28' # número do exercício
subtitulo = 'Qual número estou pensando?'# faça a pergunta do problema
cabecalho(titulo, subtitulo)
n = randint(0, 5) # Gera um número aleatório.
print('Estou pensando em um número de 0 a 5 ...')
num = int(input('Em qual número estou pensando? ')) # Usuário entra número.
sleep(3)
if num == n:
    print('Parabéns, você acertou na mosca!')
else:
    print('Que pena era {}, mais sorte da próxima vez!'.format(n))
