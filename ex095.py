equipe = list()
jogador = {}
while True:
    jogador['Nome'] = input('\033cNome do jogador: ').strip().title()
    partidas = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
    jogador['Gols'] = []
    for c in range(0, partidas):
        jogador['Gols'].append(int(input(f'Quantos gols na {c + 1}ª partida: ')))
    jogador['Total'] = sum(jogador['Gols'])
    equipe.append(jogador.copy())
    jogador.clear()
    menu = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if menu == 'N':
        break
print('-'*42)
print('Cod Nome            Gols                     Total')
print('-'*42)
for c, d in enumerate(equipe):
    print(f'{c:>3} {d['Nome']:<16}{d['Gols']}{' '*(25-(3*len(d['Gols'])))}{d['Total']}')
while True:
    print('-'*42)
    n = int(input('Mostrar dados de qual jogador? '))
    if n < len(equipe):
        print(f'O jogador {equipe[n]["Nome"]} jogou {len(equipe[n]['Gols'])} partidas.')
        for x, y in enumerate(equipe[n]['Gols']):
            if y > 0:
                print(f'        => Na {x + 1}ª partida marcou {y} gol{'s' if y > 1 else ''}.')
            else:
                print(f'        => Na {x + 1}ª partida não marcou gols.')
    elif n == 99:
        break
    else:
        print('Indíce não correspode a um jogador, tente novamente:')
print('FIM')
