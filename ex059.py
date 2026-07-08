from cores import cabecalho
from time import sleep
titulo = 'Exercício 59'
subtitulo = 'Menu interativo!'
cabecalho(titulo, subtitulo)
menu = '4'
n1 = 0
n2 = 0
while menu == '4':
    n1 = int(input('Digite o 1º número: '))
    n2 = int(input('Digite o 2º número: '))
    menu = '1'
    while menu not in ('4', '5'):
        menu = input('''O que você gostaria de fazer?
        [ 1 ] SOMAR
        [ 2 ] MULTIPLICAR
        [ 3 ] MAIOR
        [ 4 ] NOVOS NÚMEROS
        [ 5 ] SAIR
    Digite a sua opção: ''')
        if menu == '1':
            print('A soma entre {} + {} é: {}'.format(n1, n2, n1 + n2))
        elif menu == '2':
            print('O produto da multiplicação {} X {} é: {}'.format(n1, n2, n1 * n2))
        elif menu == '3':
            if n1 > n2:
                print('O maior número entre {} e {} é: {}'.format(n1, n2, n1))
            elif n1 < n2:
                print('O maior número entre {} e {} é: {}'.format(n1, n2, n2))
            else:
                print('Os número são iguais!')
        elif menu not in ('1', '2', '3', '4', '5'):
            print('Entrada inválida! Tente novamente.')
            sleep(1)
if menu == '5':
    print('Obrigado por testar! Volte sempre.')
