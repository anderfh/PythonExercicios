import cores
from random import randint
subtitulo = 'Números aleatórios numa Tupla'
linha = '- '
cores.cabsub(subtitulo, linha)
x = ()
for c in range (0,5):
    x += (randint(1,20),)
print(x)
print(f'O maior número é {max(x)}') #{sorted(x)[-1]}
print(f'O menor número é {min(x)}') #{sorted(x)[0]}
