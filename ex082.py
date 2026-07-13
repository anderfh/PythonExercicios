from cores import cabecalho
tit = 'Exercício 82'
sub = 'Separando pares e impares'
cabecalho(tit, sub)
valor = list()
while True:
    num = int(input('Digite um número: '))
    valor.append(num)
    while True:
        menu = input('Quer continuar? [S/N] ').strip().upper()[0]
        if menu in 'SN':
            break
    if menu == 'N':
        break
print(f'Lista geral: {valor}')
par = list()
impar = list()
for c in valor:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'Lista par:   {par}')
print(f'Lista impar: {impar}')
