from cores import cabecalho
titulo = 'Exercício 62'
subtitulo = 'Progressão Arritmética 3.0'
cabecalho(titulo, subtitulo)
termo = int(input('Digite o 1º termo: '))
razao = int(input('Digite a razão: '))
quant = 1
while quant > 0:
    cabecalho(titulo, subtitulo)
    print('Digite o 1º termo: {}'.format(termo))
    print('Digite a razão: {}'.format(razao))
    quant = int(input('Quantos termos calcular? '))
    soma = termo
    print('. {} '.format(soma), end='')
    while quant > 1:
        soma = soma + razao
        quant -= 1
        print('. {} '.format(soma), end='')
    print('.')
    quant = int(input('Gostaria de tentar outra quantidade? (1-Sim / 0-Não) '))
print('Obrigado por testar!')
