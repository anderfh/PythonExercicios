from cores import cabecalho
titulo = 'Exercício 80'
sub = 'Inserção de valores em lista'
cabecalho(titulo, sub)
valor = list()
n = 0
while n < 5:
    num = int(input('Digite um número: '))
    if n == 0:
        valor.append(num)
        print('Valor adicionado ao final da lista;')
    elif num >= max(valor):
        valor.append(num)
        print('Valor adicionado ao final da lista;')
    else:
        for c, v in enumerate(valor):
            if num <= v:
                valor.insert(c, num)
                print(f'Valor adicionado a posição {c}')
                break
    n += 1
print(valor)
print('-=' * 25)
print(f'Os valores digitados em ordem foram: {valor}')
