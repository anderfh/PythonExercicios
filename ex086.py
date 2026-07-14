from cores import cabecalho
tit = 'Exercício 86'
cab = 'Matriz'
cabecalho(tit, cab)
lista = [[], [], []]
for x in range(0,3):
    for y in range(0,3):
        n = int(input(f'Digite o valor para ({x}, {y}): '))
        lista[x].append(n)
for x in range(0, len(lista)):
    for y in range(0, len(lista[x])):
        print(f'[ {lista[x][y]} ]', end=' ')
    print('')        
print(f'\n\n\n{lista}')
