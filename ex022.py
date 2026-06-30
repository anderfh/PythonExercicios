nome = input('Digite um nome: ');
print('Analizando o nome ...');
print('O nome em caixa alta:  {}.'.format(nome.upper()));
print('O nome em caixa baixa: {}.'.format(nome.lower()));
print('O nome possui {} letras.'.format(len(nome)-nome.count(' ')));
corte = nome.split(' ');
pnome = corte[0];
pletras = len(pnome);
print('O primeiro nome possui {} letras.'.format(pletras));
