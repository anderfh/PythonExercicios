from cores import cabecalho
from time import sleep
titulo = 'Exercício 49'
subtitulo = 'Tabuada 2.0'
cabecalho(titulo, subtitulo)
num = int(input('Digite um número inteiro: '))
print('-- Tabuada do {} --\n'.format(num))
for c in range(1, 11):
    print('{} x {} = {}'.format(num, c, num*c))
    sleep(0.3)
print('🎆')