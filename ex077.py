import cores
subtitulo = 'Contador de vogais'
linha = '¬'
cores.cabsub(subtitulo, linha)
tupla = ('estrutura', 'codigo', 'linha', 'tempo', 'espaço', 'portugues')
for palavra in tupla:
    print(f'A palavra {palavra.upper()} tem as vogais:', end='')
    for c in range(0, len(palavra)):
        if palavra[c] in 'aeiou':
            print(f' {palavra[c]}', end='')
    print('.')
print(' ----- FIM ----- ')
