r1 = float(input('Digite o tamanho da 1ª reta: '))
r2 = float(input('Digite o tamanho da 2ª reta: '))
r3 = float(input('Digite o tamanho da 3ª reta: '))
lista = sorted((r1, r2, r3))
if (r1 + r2 + r3) > (lista[2]*2):
    print('As 3 linhas podem formar um triângulo!')
else:
    print('As linhas não podem formar um triângulo')
