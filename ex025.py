nome = str(input('Digite o nome: ')).strip();
print('O indivíduo possui Silva no nome? {}'.format((nome.upper()+' ').count('SILVA ') > 0));
