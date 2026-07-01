print(' --- Exercício 31 ---')
print('-- Cálculo Passagem --\n')
dis = float(input('Qual a distância do destino em Km? '))//1
valor = dis*0.5 if dis < 200 else dis*0.45
print('\nO valor da passagem é R${:.2f}.'.format(valor))
