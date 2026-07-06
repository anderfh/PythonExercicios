from cores import cabecalho
from time import sleep
titulo = 'Exercício 48'
subtitulo = 'Contagem Restritiva'
cabecalho(titulo, subtitulo)
soma = 0
for c in range(1, 501):
    if c % 2 == 1:
        if c % 3 == 0:
            soma += c
print(soma)