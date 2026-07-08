from cores import cabecalho
titulo = 'Exercício 63'
subtitulo = 'Sequencia de Fibonacci'
cabecalho(titulo, subtitulo)
n = int(input('Digite quantos termos quer: '))
n0 = 0
n1 = 0
n2 = 1
if n >= 1:
    print('. {} '.format(n1), end='')
while n >= 2:
    print('. {} '.format(n2), end='')
    n0 = n1
    n1 = n2
    n2 = n1 + n0
    n -= 1
print('.')