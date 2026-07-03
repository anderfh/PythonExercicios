from cores import cabecalho
from time import sleep
from datetime import date
titulo = 'Exercício 39'
subtitulo = 'Alistamento Militar, e aí?'
cabecalho(titulo, subtitulo)

anoNasc = int(input('Qual o seu ano de nascimento? '))
atual = date.today().year
ali = '\033[1;32malistamento militar\033[m'
print('\nAnalisando ...\n')
sleep(1)
if atual == anoNasc + 18:
    print(f'Está na hora de fazer o seu {ali}!')
elif atual < anoNasc + 18:
    print('O seu {} está próximo, faltam {} anos.'.format(ali, 18 - (atual - anoNasc)))
else:
    print('O seu {} foi no ano de {}'.format(ali, anoNasc + 18))