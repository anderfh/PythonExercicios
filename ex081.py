from cores import cabecalho
tit = 'Exercício 81'
sub = 'Extrato de uma lista'
cabecalho(tit, sub)
valor = list()
while True:
    num = int(input('Digite um número: '))
    valor.append(num)
    while True:
        menu = input('Quer continuar? [S/N] ').strip().upper()[0]
        if menu in 'SN':
            break
    if menu == 'N':
        break
print(f'Foram digitados {len(valor)} números.')
valor.sort(reverse=True)
print(f'Os valores em ordem decrescente: {valor}')
if 5 in valor:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista')
