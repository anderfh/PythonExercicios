from cores import cabecalho
from time import sleep
titulo = 'Exercício 52'
subtitulo = 'É um número primo?'
cabecalho(titulo, subtitulo)
num = int(input('Digite o número: '))
print('Analisando ...')
sleep(2)
resultado = 'Primo !'
if num > 3:
    if num % 2 != 0:
        for c in range(3, num-1, 2):
            if num % c == 0:
                resultado = 'NÃO é primo !'
    else:
        resultado = 'NÃO é primo !'
print(resultado)
