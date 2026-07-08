from cores import cabecalho
from datetime import date
from idade import idade
titulo = 'Exercício 54'
subtitulo = 'Quem já é maior?'
cabecalho(titulo, subtitulo)
maior = 0
for c in range(0,7):
    idad = idade(input('Qual a sua data de nascimento? (dd/mm/aaaa) '))
    if idad > 21:
        maior += 1
print(maior)
