from cores import cabecalho
titulo = 'Exercício 55'
subtitulo = 'Qual o maior e menor peso?'
cabecalho(titulo, subtitulo)
maior = 0
menor = 0
for c in range(0,5):
    peso = int(input('Peso {} (kg): '.format(c+1)))
    if c == 0:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O menor peso foi {}Kg, e o maior peso foi {}kg.'.format(menor, maior))
