def cabecalho(titulo, subtitulo):
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