import cores
subtitulo = 'Número por extenso'
linha = '-=-'
tupla = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    menu = 'S'
    cores.cabsub(subtitulo, linha)
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {cores.cor['vrm']}{tupla[n].upper()}{cores.cor['lmp']}.\n')
    while True:
        menu = input('Você gostaria de digitar outro número? (S/N) ').upper().strip()[0]
        if menu in 'SN':
            break
    if menu == 'N':
        break
