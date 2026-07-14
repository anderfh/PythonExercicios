import cores
tit = 'Exercício 89'
sub = 'Boletim escolar'
cores.cabecalho(tit, sub)
escola = list() # aluno
while True:
    nome = (input('Nome: ').strip().title())
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    media = (nota1 + nota2) / 2
    escola.append([nome, [nota1, nota2], media])
    while True:
        menu = input('Deseja continuar? [S/N]: ').strip().upper()[0]
        if menu in 'SN':
            break
    if menu == 'N':
        break
linha = '-'
cores.cabsub(sub, linha)
print(' Nº| Nome          | Média')
print('--------------------------')
for c in range(0, len(escola)):
    print(f' {c + 1} | {escola[c][0]:<14}| {escola[c][2]:.1f}')
while True:
    menu = int(input('\nGostaria de ver as notas de qual aluno? (99 interrompe): '))
    if menu <= len(escola):
        print(f'As notas de {escola[menu - 1][0]} foram: {escola[menu - 1][1]}')
    elif menu == 99:
        break
