from cores import cabecalho
from random import randint
from time import sleep
titulo = 'Exercício 58' # número do exercício
subtitulo = 'Qual número estou pensando? 2.0'# faça a pergunta do problema
cabecalho(titulo, subtitulo)
n = randint(0, 5) # Gera um número aleatório.
print('Estou pensando em um número de 0 a 5 ...')
cont = 0
cond = False
while not cond:
    if cont != 0:
        print('Errou, tente novamente!')
        sleep(0.6)
    num = int(input('Em qual número estou pensando? ')) # Usuário entra número.
    if num == n:
        cond = True
    cont += 1
    sleep(1)
if cont == 1:
    print('Parabéns, você acertou na mosca!')
else:
    print('Você acertou após {} tentativas.'.format(cont))
