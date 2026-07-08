from cores import cabecalho
from time import sleep
titulo = 'Exercício 53'
subtitulo = 'É um palindromo?'
cabecalho(titulo, subtitulo)
frase = input('Digite uma frase: ').upper().strip(' .,-').split(' ')
junta = ''.join(frase)
palindromo = 'SIM !!'
for c in range(0, len(junta)):
    if junta[c] != junta[(c*(-1))-1]:
        palindromo = 'NÃO :('
print(junta)
print('É um palíndromo? {}'.format(palindromo))
