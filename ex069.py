from cores import cabecalho
titulo = 'Exercício 69'
subtitulo = 'Cadastro interativo'
maior = 0
homem = 0
garota = 0
cont = 0
while True:
    cabecalho(titulo, subtitulo)
    print(f'{'-'*25}\n   Cadastre uma pessoa   \n{'-'*25}')
    idade = int(input('Qual a idade? '))
    while True:
        sexo = input('Qual o sexo? (M/F) ').strip().upper()[0]
        if sexo in 'MF':
            break
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        garota += 1
    cont += 1
    menu = ' '
    while menu not in 'SN':
        menu = input('Quer continuar digitando? (S/N) ').strip().upper()[0]
    if menu == 'N':
        break
cabecalho(titulo, subtitulo)
print(f'{'-'*25}\n{'Resultado final':^25}\n{'-'*25}')
print(f'{cont} pessoas cadastradas, sendo:\n    {maior} pessoas maiores de 18 anos;\n    {homem} homens;\n    {garota} mulheres com menos de 20 anos.')
