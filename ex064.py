from cores import cabecalho
titulo = 'Exercício 64'
subtitulo = '999'
cabecalho(titulo, subtitulo)
num = 0
soma = 0
cont = 0
num = int(input('Digite um número: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número: '))
print('Foram digitados {} números, totalizando {}.'.format(cont, soma))
