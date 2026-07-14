from cores import cabecalho
tit = 'Exercício 87'
cab = 'Analize de matriz'
cabecalho(tit, cab)
lista = [[], [], []]
for x in range(0,3):
    for y in range(0,3):
        n = int(input(f'Digite o valor para ({x}, {y}): '))
        lista[x].append(n)
somapar = 0
somacol = 0
for x in range(0, len(lista)):
    for y in range(0, len(lista[x])):
        z = lista[x][y]
        print(f'[ {z} ]', end=' ')
        if z % 2 == 0:
            somapar += z
        if y == 2:
            somacol += z
    print('')
print(f'A soma dos valores pares resulta em {somapar}.')
print(f'A soma dos valores da 3ª coluna é {somacol}.')
print(f'O maior valor da 2ª linha é {max(lista[1])}')
print(f'\n\n\n{lista}')
