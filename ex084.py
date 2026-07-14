from cores import cabecalho
tit = 'Exercício 84'
sub = 'Lista dentro de lista'
cabecalho(tit, sub)
lista = list()
dados = list()
while True:
    dados.append(input('Nome: ').strip().title())
    dados.append(int(input('Peso: ')))
    lista.append(dados[:])
    dados.clear()
    while True:
        menu = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if menu in 'SN':
            break
    if menu == 'N':
        break
print(lista)
print(f'Foram cadastradas um total de {len(lista)} pessoas.')
peso = list()
for c in lista:
    peso.append(c[1])
peso.sort()
mais = list()
menos = list()
for l in range(0, len(lista)):
    if lista[l][1] == max(peso):
        mais.append(lista[l][0])
for l in range(0, len(lista)):
    if lista[l][1] == min(peso):
        menos.append(lista[l][0])
print(f'As pessoas mais pesadas com {peso[-1]:.1f}kg são {mais}')
print(f'As pessoas mais leves com {peso[0]:.1f}kg são {menos}')
