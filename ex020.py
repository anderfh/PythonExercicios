from random import shuffle
print('--- Exercício 20 ---')
print('-- Lista aleatória --')
al1 = (input('Digite o nome do primeiro aluno: '))
al2 = (input('Digite o nome do segundo aluno: '))
al3 = (input('Digite o nome do terceiro aluno: '))
al4 = (input('Digite o nome do último aluno: '))
lista = [al1, al2, al3, al4]
shuffle(lista)
print('A ordem de apresentação será:\n{}\n{}\n{}\n{}'.format(lista[0], lista[1], lista[2], lista[3]))