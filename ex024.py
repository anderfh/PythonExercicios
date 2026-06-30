cidade = str(input('Diga o nome de uma cidade: ')).strip();
print('A cidade começa com Santo? {}'.format(cidade.lower().split(' ')[0] == 'santo'));
