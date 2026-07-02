from cores import cabecalho
titulo = 'Exercício 37'
subtitulo = 'Que número é esse?'
cabecalho(titulo,subtitulo)
num = int(input('Qual número você gostaria de converter? '))
base = int(input('''Para qual base gostaria de converter?
    1 - Binária
    2 - Octal
    3 - Hexadecimal
Digite o número do menu: '''))
if base == 1:
    print('\033[1m {}'.format(bin(num)[2:]))
elif base == 2:
    print('\033[1m {}'.format(oct(num)[2:]))
elif base == 3:
    print('\033[1m {}'.format(hex(num)[2:]))
else:
    print('Opção inválida!')