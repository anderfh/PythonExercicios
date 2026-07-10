import cores
subtitulo = 'LISTAGEM DE PREÇO'
linha = '-'
cores.cabsub(subtitulo, linha)
produtos = ('régua', 0.50,
            'folha A4', 12.50,
            'caneta', 1.30,
            'lápis', 0.80,
            'post-it', 3.75,
            'carimbo', 57.80,
            'marca texto', 6.89,
            'mouse', 89.95,
            'notebook', 2349.87,
            'impressora', 5750.00,
            'celular', 1654.32)
for c in range(0,len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c].capitalize():.<40}', end='')
    else:
        print(f'R${produtos[c]:>8.2f}')
print('-'*50)
