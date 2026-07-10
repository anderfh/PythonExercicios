import cores
subtitulo = 'Lendo números e classificando'
linha = '¹²³²'
cores.cabsub(subtitulo, linha)
x = ()
for c in range (1,5):
    x += (int(input(f'Digite o {c}º número de 0 à 9: ')),)
print(x)
print(f'O valor 9 apareceu {cores.cor['nazl']}{x.count(9)}{cores.cor['lmp']} vezes;')
if 3 in x:
    print(f'O valor 3 aparece pela 1ª vez na {cores.cor['nazl']}{x.index(3) + 1}{cores.cor['lmp']}ª posição;')
else:
    print('Não foi digitado nenhum valor 3;')
cont = 0
for n in x:
    if n % 2 == 0:
        if cont == 0:
            print('Valor(es) par:', end='')
        cont +=1
        if cont > 1:
            print(' e', end ='')
        print(f' {n}', end='')
if cont == 0:
    print('Não foram digitados valores pares.')
else:
    print('.')