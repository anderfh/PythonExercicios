frase = str(input('Digite uma frase: ')).strip().upper();
letra = str(input('Qual letra deseja procurar na frase? ')).strip().upper()[0];
print('A letra \"{}\" aparece {} vezes na frase.'.format(letra, frase.count(letra)));
print('A letra \"{}\" aparece pela primeira vez na posição {}.'.format(letra, frase.index(letra)+1));
print('A letra \"{}\" aparece pela última vez na posição {}.'.format(letra, frase.rindex(letra)+1));
