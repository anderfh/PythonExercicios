from math import radians, sin, cos, tan
print('--- Exercício 18 ---')
ang = float(input('Digite o angulo em graus: '))
rad = radians(ang) #Converte graus para radianos.
print('O seno de {}° é {:.4f}'.format(ang, sin(rad)))
print('O cosseno de {}° é {:.4f}'.format(ang, cos(rad)))
print('A tangente de {}° é {:.2f}'.format(ang, tan(rad)))
