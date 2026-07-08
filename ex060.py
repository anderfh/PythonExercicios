from cores import cabecalho
from time import sleep
titulo = 'Exercício 60'
subtitulo = 'Fatorial !'
cabecalho(titulo, subtitulo)
n = int(input('Digite o número que gostaria de fatorar: '))
soma = 1
cont = n
while cont > 0:
    print('{}'.format(cont), end='')
    print(' X ' if cont > 1 else ' = ', end='')
    soma *= cont
    cont -= 1
print('{}'.format(soma))
