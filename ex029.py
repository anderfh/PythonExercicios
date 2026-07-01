v = float(input('Velocidade atual (Km/h): '))
if v > 80:
    print('Você ultrapassou o limite de velocidade de 80 Km/h.')
    print('O valor da multa será de R${:.2f}'.format((v-80)*7))
print('Tenha um bom dia! Dirija com segurança.')
