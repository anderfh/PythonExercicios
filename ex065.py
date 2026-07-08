from cores import cabecalho
titulo = 'Exercício 65'
subtitulo = 'Super contador!'
menu = '1'
soma = 0
cont = 0
maior = 0
menor = 0
while menu != '0':
    while menu == '1':
        cabecalho(titulo, subtitulo)
        if cont == 0:
            num = int(input('Digite o 1º número: '))
            soma = num
            cont += 1
            maior = num
            menor = num
        num = int(input('Digite outro número: '))
        soma += num
        cont += 1
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        menu = '2'
        while menu not in ('0', '1'):
            menu = input('Quer adicionar mais números? (1-SIM / 0- NÃO) ')
            if menu not in ('0', '1'):
                print('Entrada inválida, tente outra vez.')
cabecalho(titulo, subtitulo)
print('''Você digitou {} números.
A média de valor é {:.2f}
O maior valor foi {}
O menor valor foi {}'''.format(cont, soma/cont, maior, menor))
