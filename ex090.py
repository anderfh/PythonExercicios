print('\033c', end='')
aluno = dict()
aluno['nome'] = input('Nome: ').strip().title()
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno["média"] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'
print(aluno)
for k, v in aluno.items():
    print(f'{k.capitalize()} é igual a {v}')
