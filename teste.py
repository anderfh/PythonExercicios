equipe = [{'nome': 'Anderson', 'gols': [1, 2, 3], 'total': 6}]
print('-'*40)
for c, d in enumerate(equipe):
    print(f'{c:>3} {d['nome']:<16} {d['gols']}{' ' * (16 - (3 * 3))}{d['total']}')