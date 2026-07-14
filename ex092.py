from datetime import date
pessoa = {}
pessoa['Nome'] = input('\033cNome: ').strip().title()
pessoa['Idade'] = date.today().year - int(input('Data de nascimento: '))
pessoa['CTPS'] = int(input('Carteira de trabalho: (0 não tem): '))
if pessoa["CTPS"] > 0:
    pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = 'R$ ' + input('Salário: (R$) ')
    pessoa['Aposentadoria'] = 35 + pessoa['Idade'] - (date.today().year - pessoa['Ano de contratação'])
for k, v in pessoa.items():
    print(f'     {k} tem o valor {v}')
print(pessoa)
