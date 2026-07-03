from cores import cabecalho
from time import sleep
titulo = 'Exercício 40'
subtitulo = 'Qual a minha média escolar?'
cabecalho(titulo, subtitulo)
print('Digite as notas para calcular a média.')
nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
media = (nota1 + nota2)/2
print('Calculando ...')
sleep(1)
print('A sua média é \033[1m{:.1f}\033[m'.format(media))
sleep(1)
print('Analizando ...')
sleep(2)
if media < 5.0:
    print('\033[1;41m REPROVADO :( \033')
elif media < 7.0:
    print('\033[1;44m Em recuperação :| \033')
else:
    print('\033[1;42m APROVADO :) \033')
