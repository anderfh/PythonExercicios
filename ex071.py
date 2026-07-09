print(f'\033c{'-'*50}\n{'Caixa Eletrônico':^50}\n{'-'*50}')
valor = int(input('Qual o valor você gostaria de sacar? R$'))
cinq = 0
vint = 0
dez = 0
um = 0
while valor > 0:
    while valor >= 10:
        while valor >= 20:
            while valor >= 50:
                cinq += 1
                valor -= 50
            if valor < 20:
                break
            vint +=1
            valor -= 20
        if valor < 10:
            break
        dez += 1
        valor -= 10
    if valor < 1:
        break
    um += 1
    valor -= 1
if cinq > 0:
    print(f'Total de {cinq} de R$50')
if vint > 0:
    print(f'Total de {vint} de R$20')
if dez > 0:
    print(f'Total de {dez} de R$10')
if um > 0:
    print(f'Total de {um} de R$1')
