from cores import cabecalho
tit = 'Exercício 85'
sub = 'Pares e impares numa lista crescente'
cabecalho(tit, sub)
lista = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print(lista)
print(f'Os números pares são: {sorted(lista[0])}')
print(f'Os números impares são: {sorted(lista[1])}')
