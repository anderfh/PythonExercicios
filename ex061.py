from cores import cabecalho
titulo = 'Exercício 61'
subtitulo = 'Progressão Arritmética 2.0'
cabecalho(titulo, subtitulo)
termo = int(input('Digite o 1º termo: '))
razao = int(input('Digite a razão: '))
quant = int(input('Quantos termos calcular? '))
soma = termo
print('. {} '.format(soma), end='')
while quant > 1:
    soma = soma + razao
    quant -= 1
    print('. {} '.format(soma), end='')
print('.')
