from cores import cabecalho
titulo = 'Exercício 56'
subtitulo = 'Quem é quem?'
idades = 0
hidade = 0
homem = 'Fulano'
mulheres = 0
for c in range(0,4):
    cabecalho(titulo, subtitulo)
    print('--- Indivíduo nº {} ---'.format(c+1))
    nome = input('--- Nome: ')
    idade = int(input('--- Idade: '))
    sexo = input('Sexo (m/f): ').upper().strip()
    idades += idade
    if sexo[0] == 'M':
        if idade > hidade:
            hidade = idade
            homem = nome
    elif sexo[0] == 'F':
        if idade < 20:
            mulheres += 1
    else:
        print('Entrada inválida!')
cabecalho(titulo, subtitulo)
print('A média de idade do grupo é: {}.'.format(idades/4))
print('O homem mais velho é {} com {} anos.'.format(homem, hidade))
print('No total são {} mulheres com menos de 20 anos.'.format(mulheres))
