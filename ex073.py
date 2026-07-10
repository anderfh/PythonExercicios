import cores
subtitulo = 'Tabela brasileirão'
linha = '° o '
cores.cabsub(subtitulo, linha)
brasil = ('Pal', 'Fla', 'Flu', 'APR', 'Bra', 'Bah', 'Ctb',
          'SPa', 'AMG', 'Cor', 'Cru', 'Bot', 'Vit', 'Int',
          'San', 'Gre', 'Vas', 'Rem', 'Mir', 'Cha')
print(f'Os cinco primeiro colocados são: {brasil[:5]}')
print(f'Os últimos quatro colocados são: {brasil[-4:]}')
print(f'Os times em ordem alfabética :   {sorted(brasil)}')
print(f'O time da Chapecoense está na {(brasil.index('Cha')) + 1}ª posição.')