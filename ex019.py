from random import randint
print('--- Exercício 19 ---')
print('-- Escolha aleatória --')
al1 = (input('Digite o nome do primeiro aluno: '))
al2 = (input('Digite o nome do segundo aluno: '))
al3 = (input('Digite o nome do terceiro aluno: '))
al4 = (input('Digite o nome do último aluno: '))
esc = randint(1,4)
lista = [al1, al2, al3, al4]
print('O aluno escolhido foi {}'.format(lista[esc]))
