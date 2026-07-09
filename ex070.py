print('\033c')
print(f'{'-'*50}\n{'Lojão Virtual':^50}\n{'-'*50}')
total = 0
mil = 0
nomemenor = ''
barato = 0
while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preço do produto (R$): ').replace(',', '.'))
    if total == 0:
        barato = preco
    total += preco
    if preco > 1000:
        mil += 1
    if preco <= barato:
        barato = preco
        nomemenor = nome
    while True:
        menu = input('Deseja continuar? (s/n) ').strip().lower()[0]
        if menu in 'sn':
            break
    if menu == 'n':
        break
print('-'*50)
print(f'Total da compra = {total:.2f};\nForam adquiridos {mil} produtos que custam mais de R$1.000,00;\nO produto mais barato foi {nomemenor} que custou R${barato:.2f}.')