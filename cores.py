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
        'nazl':'\033[1;34m'
    }

def cabecalho(titulo, subtitulo):
    print('\033c' + '{}'.format(cor['bazl']) + '°oO' * 20 + '{}'.format(cor['lmp']) + '{}'.format(cor['azl']))
    print('-'*23 + ' ' + titulo + ' ' +'-'*23)
    print('{}'.format(cor['vrm']) + '-' * (29 - (len(subtitulo) // 2)) + ' ' + subtitulo + ' ' + '-' * (29 - (len(subtitulo) // 2)))
    print(cor['lmp'])

def cabsub(subtitulo, linha):
    print('\033c', end='')
    print(linha * (50 // len(linha)) + linha[:(50 % len(linha))])
    if len(subtitulo) > 50:
        print(subtitulo[:50])
    else:
        print(f'{cor['nazl']}{subtitulo:^50}{cor['lmp']}')
    print(linha * (50 // len(linha)) + linha[:(50 % len(linha))])
    print(cor['lmp'])
