from cores import cabecalho
from time import sleep
titulo = 'Exercício 43'
subtitulo = 'Qual o meu IMC?'
cabecalho(titulo, subtitulo)
peso = float(input('Qual o seu peso? (kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura * altura)
print('\n O seu IMC é: {:.1f}'.format(imc))
print('Analizando ...')
sleep(2)
if imc < 18.5:
    print('\033[1;44m Abaixo do Peso :( \033')
elif imc < 25:
    print('\033[1;42m Peso Ideal :) \033')
elif imc < 30:
    print('\033[1;43m Sobrepeso :| \033')
elif imc < 40:
    print('\033[1;44m Obesidade :( \033')
else:
    print('\033[1;47m Obesidade Mórbida :( \033')
