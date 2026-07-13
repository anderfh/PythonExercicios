from cores import cabecalho
tit = 'Exercício 83'
sub = 'Analizando uma expressão'
cabecalho(tit, sub)
exp = list(input('Digite a expressão: '))
abre = 0
fecha = 0
for c in exp:
    if c == '(':
        abre += 1
    elif c == ')':
        fecha += 1
    if fecha > abre:
        break
if fecha == abre:
    print(' expressão está correta !')
else:
    print('A expressão está incorreta :(')
