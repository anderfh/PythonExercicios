from cores import cabecalho
from time import sleep
titulo = 'Exercício 46'
subtitulo = 'Contagem Regressiva'
cabecalho(titulo, subtitulo)
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('🎆')