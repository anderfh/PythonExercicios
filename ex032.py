ano = int(input('Digite o ano: '))
if ano > 1582:
    if ano % 4 == 0:
        if ano % 100 != 0:
            print('Ano Bissexto')
        elif ano % 400 == 0:
            print('Ano Bissexto')
        else:
            print('Não é ano bissexto')
    else:
        print('Não é ano bissexto')
else:
    print('O cálculo não se aplica a datas anteriores a 1582.')
