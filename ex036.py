from cores import cabecalho
titulo = 'Exercício 36'
subtitulo = 'Consigo um empréstimo?'
cabecalho(titulo, subtitulo)
valorCasa = float(input('Qual o valor do Imóvel? '))
salario = float(input('Qual a sua média salarial? '))
meses = int(input('Em quanto tempo gostaria de pagar? (ex: {:.0f} meses) '.format((valorCasa/(salario*0.3))//1)))
if (salario * 0.3) > (valorCasa/meses):
    print('A prestação será de R${:.2f}.'.format(valorCasa/meses))
else:
    print('Empréstimo negado, motivo: Renda insuficiente')