print('--- Exercício 11 ---')
print('-- Quantidade de tinta --')
alt = float(input('Altura da parede em metros: '))
lar = float(input('Largura da perede em metros: '))
rnd = 2 #Rendimento da lata de tinta
print('A parede tem {:.2f}m² e serão necessárias {:.1f} latas de tinta.'.format(alt*lar, (alt*lar)/rnd))