from cores import cabecalho
from time import sleep
titulo = 'Exercício 57'
subtitulo = 'Tente outra vez!'
sexo = ''
while sexo not in ('M', 'F'):
    cabecalho(titulo, subtitulo)
    if sexo != '':
        print('Entrada inválida.\nTente outra vez!\n')
        sleep(0.6)
    sexo = input('Digite o sexo (F/M): ').upper().strip()[0]
print('Segue o baile !!!')