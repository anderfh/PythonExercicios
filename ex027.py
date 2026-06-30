nome = input('Digite o nome: ').strip();
corte = nome.split(' ');
print('Primeiro nome: {}'.format(corte[0]));
print('Último nome:   {}'.format(corte[-1]));
