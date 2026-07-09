from cores import cabecalho
titulo = 'Exercício 66'
subtitulo = '999 break'
cabecalho(titulo, subtitulo)
cont = 0
soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Você digitou {cont} números, a soma deles é {soma}.')
