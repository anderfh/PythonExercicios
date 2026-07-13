from cores import cabecalho
titulo = 'Exercício 79'
subtitulo = 'Lista limitada'
cabecalho(titulo, subtitulo)
valor = list()
while True:
    num = int(input('Digite um valor: '))
    if num not in valor:
        valor.append(num)
        print(' Valor adicionado com sucesso!')
    else:
        print(' Valor duplicado! Não será adicionado.')
    menu = 'H'
    while menu not in 'SN':
        menu = input('Quer continuar a adicionar valores? (S/N) ').strip().upper()[0]
    if menu == 'N':
        break
valor.sort()
print(f'Você digitou os valores: {valor}')
print('FIM')
