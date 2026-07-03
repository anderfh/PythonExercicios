from cores import cabecalho
from time import sleep
from datetime import date
titulo = 'Exercício 41'
subtitulo = 'Qual a minha categoria de natação?'
cabecalho(titulo, subtitulo)
data = input('Qual a sua data de nascimento? (dd/mm/aaaa) ').split('/')
datanasc = date(int(data[2]), int(data[1]), int(data[0]))
hoje = date.today()
idade = (hoje.year - datanasc.year)
if (datanasc.month, datanasc.day) >= (hoje.month, hoje.day):
    idade -= 1
print('A sua categoria é:')
sleep(2)
if idade < 9:
    print('\033[1;43m Mirim :) \033')
elif idade < 14:
    print('\033[1;44m Infantil :) \033')
elif idade < 19:
    print('\033[1;45m Junior :) \033')
elif idade < 40:
    print('\033[1;46m Sênior :) \033')
else:
    print('\033[1;42m Master :) \033')
