jogador = {}
jogador['Nome'] = input('\033cNome do jogador: ').strip().title()
partidas = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
jogador['Gols'] = []
for c in range(0, partidas):
    jogador['Gols'].append(int(input(f'Quantos gols na {c + 1}ª partida: ')))
jogador['Total'] = sum(jogador['Gols'])
print('-'*30)
print(jogador)
print('-'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-'*30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for x, y in enumerate(jogador['Gols']):
    if y > 0:
        print(f'        => Na {x + 1}ª partida marcou {y} gol{'s' if y > 1 else ''}.')
    else:
        print(f'        => Na {x + 1}ª partida não marcou gols.')
print(f'Foi um total de {jogador["Total"]} gol{'s' if jogador["Total"] > 1 else ''}.')
