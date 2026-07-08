from cores import cabecalho
from time import sleep
titulo = 'Exercício 50'
subtitulo = 'Soma de pares'
cabecalho(titulo, subtitulo)
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print('A soma é ...')
sleep(1)
if cont == 0:
    print('Você não informou nenhum número par')
elif cont == 1:
    print('Você informou apenas 1 número par de valor {}'.format(soma))
else:
    print('Você informou {} números pares e a soma é {}.'.format(cont, soma))
