titulo = 'Exercício 35'
subtitulo = 'Pode ser um triângulo?'
cor = {
    'lmp':'\033[m',
    'brn':'\033[30m',
    'vrm':'\033[31m',
    'vrd':'\033[32m',
    'amr':'\033[33m',
    'azl':'\033[34m',
    'rxo':'\033[35m',
    'cno':'\033[36m',
    'cnz':'\033[37m',
    'bprt':'\033[7;40m',
    'bazl':'\033[44m',
}
print('\033c' + '{}'.format(cor['bazl']) + '°oO' * 20 + '{}'.format(cor['lmp']) + '{}'.format(cor['azl']))
print('-'*23 + ' ' + titulo + ' ' +'-'*23)
print('{}'.format(cor['vrm']) + '-' * (29 - (len(subtitulo) // 2)) + ' ' + subtitulo + ' ' + '-' * (29 - (len(subtitulo) // 2)))
print(cor['lmp'])
r1 = float(input('Digite o tamanho da 1ª reta: '))
r2 = float(input('Digite o tamanho da 2ª reta: '))
r3 = float(input('Digite o tamanho da 3ª reta: '))
lista = sorted((r1, r2, r3))
if (r1 + r2 + r3) > (lista[2]*2):
    print('As 3 linhas podem formar um triângulo!')
else:
    print('As linhas não podem formar um triângulo')
