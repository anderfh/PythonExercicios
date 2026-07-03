from cores import cabecalho
from time import sleep
titulo = 'Exercício 44'
subtitulo = 'Tem desconto?'
cabecalho(titulo, subtitulo)
preco = float(input('Qual o preço do produto? '))
pag = input('''Qual a forma de pagamento?
    1 - Dinheiro
    2 - Cartão á vista
    3 - Cartão 2x
    4 - Cartão 3x ou mais
Escolha a forma de pagamento: ''')
sleep(2)
valor = preco
com = '.'
if pag == '1':
    valor = preco * 0.9
    com = ', você ganhou 10% de desconto!'
elif pag == '2':
    valor = preco * 0.95
    com = ', você ganhou 5% de desconto!'
elif pag == '4':
    valor = preco * 1.2
    com = ', acréscimo de 20% de juros.'
elif pag == '3':
    valor = preco
else:
    print('erro')
print('O valor fica R${:.2f}{}'.format(valor, com))