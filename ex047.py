from cores import cabecalho
from time import sleep
titulo = 'Exercício 47'
subtitulo = 'Contagem de Pares'
cabecalho(titulo, subtitulo)
for c in range(2, 51, 2):
    print('{} '.format(c), end = '')
print('🎆')