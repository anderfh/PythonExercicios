print('-- cálculo de aumento --')
sal = float(input('Digite seu salário atual: '))
aum = 10 if sal > 1250 else 15
print(' O seu aumento será de {}%\nSeu salário passará a ser de R${:.2f}'.format(aum, sal*aum/100+sal))
