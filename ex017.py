from math import pow, sqrt
print('--- Exercício 17 ---')
print('-- Cálculo da Hipotenusa --\n')
cata = float(input('Digite o valor do cateto a: '))
catb = float(input('Digite o valor do cateto b: '))
hipo = sqrt((pow(cata, 2))+(pow(catb, 2)))
print('A hipotenusa do triangulo retângulo é {:.2f}'.format(hipo))
