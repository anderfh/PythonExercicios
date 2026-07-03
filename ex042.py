from cores import cabecalho
from time import sleep
titulo = 'Exercício 42'
subtitulo = 'Pode ser um triângulo? Qual?'
cabecalho(titulo, subtitulo)
r1 = float(input('Digite o tamanho da 1ª reta: '))
r2 = float(input('Digite o tamanho da 2ª reta: '))
r3 = float(input('Digite o tamanho da 3ª reta: '))
lista = sorted((r1, r2, r3))
pode = ' '
qual = ':('
if (r1 + r2 + r3) <= (lista[2]*2):
    pode = ' não '
elif r1 == r2 == r3:
    qual = 'equilátero'
elif r1 == r2 or r1 == r3 or r2 == r3:
    qual = 'isóceles'
else:
    qual = 'escaleno'
print('Analisando ...')
sleep(2)
print('As linhas{}podem formar um triângulo {}.'.format(pode, qual))