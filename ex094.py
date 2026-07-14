cliente = list()
pessoa = dict()
while True:
    pessoa['nome'] = input('\033cNome: ').strip().title()
    while True:
        pessoa['sexo'] = input('Sexo: ').strip().upper()[0]
        if pessoa['sexo'] in 'FM':
            break
    pessoa['idade'] = int(input('Idade: '))
    cliente.append(pessoa.copy())
    pessoa.clear()
    menu = input('Deseja continuar? (S/N): ').strip().upper()[0]
    if menu == 'N':
        break
print(f'   a) Foram cadastradas {len(cliente)} pessoas.')
tidade = 0
for c, d in enumerate(cliente):
    tidade += cliente[c]['idade']
midade = tidade / len(cliente)
print(f'   b) A média de idade é de {tidade / len(cliente):.1f} anos.')
mulheres = list()
for c, d in enumerate(cliente):
    if cliente[c]['sexo'] == 'F':
        mulheres.append(cliente[c]['nome'])
print(f'   c) As mulheres cadastradas são: {mulheres}')
print(f'   d) Os clientes mais velhos são:')
for c, d in enumerate(cliente):
    if cliente[c]['idade'] > midade:
        print(f'      - {cliente[c]['nome']} com {cliente[c]['idade']} anos;')
print(cliente)
