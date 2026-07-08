from cores import cabecalho
from time import sleep
titulo = 'Exercício 51'
subtitulo = 'Progressão Arritmética'
cabecalho(titulo, subtitulo)
num = int(input('Digite o número inicial: '))
razao = int(input('Digite a razão da PA: '))
linhas = int(input('Digite o número de linhas: '))
print('Calculando ...')
sleep(2)
print('1 --> {}'.format(num))
sleep(0.3)
for c in range(1, linhas):
    num += razao
    print('{} --> {}'.format(c+1, num))
    sleep(0.3)
