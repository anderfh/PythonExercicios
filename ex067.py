from cores import cabecalho
titulo = 'Exercício 67'
subtitulo = 'Tabuada 3.0'
cabecalho(titulo, subtitulo)
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print(f'{'-'*30}\n  Tabuada do {n}:\n{'-'*30}')
    for c in range(1,11):
        print(f'    {n} x {c} = {n*c}')
print('Você saiu do programa Tabuada 3.0')
