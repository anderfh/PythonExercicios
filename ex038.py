from cores import cabecalho
from time import sleep
titulo = 'Exercício 38'
subtitulo = 'Qual número é maior?'
cabecalho(titulo, subtitulo)
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
print('Analisando ...')
sleep(2)
if n1 == n2:
    print('Não há número maior, ambos são iguais!')
elif n1 > n2:
    print('O primeiro número é maior!')
else:
    print('O segundo número é maior!')
