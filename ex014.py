print('--- Exercício 14 ---')
print('-- Conversor de Temperatura --')
cel = float(input('Digite a temperatura em °C: '))
far = cel*1.8+32
kel = cel+273.15
print('\n{}°C equivale a {:.1f}°F e a {:.2f}K.'.format(cel, far, kel))