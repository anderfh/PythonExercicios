from random import randint
print('\033c')
num = list()
n = 0
while n < 5:
    # num.append(randint(0,9))
    num.append(int(input(f'Digite o valor da posição {n}: ')))
    n += 1
print(num)
print(f'O maior número é: {max(num)} e se encontra nas posições: ', end='')
cont = 0
for c, v in enumerate(num):
    if v == max(num):
        if cont == 0:
            print(f'{c}', end='')
        else:
            print(f', {c}', end='')
        cont += 1
print('.')
print(f'O menor número é: {min(num)} e se encontra nas posições: ', end='')
cont = 0
for c, v in enumerate(num):
    if v == min(num):
        if cont == 0:
            print(f'{c}', end='')
        else:
            print(f', {c}', end='')
        cont += 1
print('.')
print('END')
