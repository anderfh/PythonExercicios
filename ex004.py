algo = input('Digite algo = ')
print('Você digitou = {}'.format(algo))
formato = type(algo)
print('o tipo primitivo é =', formato)
if algo.isnumeric():
    print('É um número')
elif algo.isalpha():
    if algo.isupper():
        print('É alfabético em maiúsculas')
    elif algo.islower():
        print('É alfabético em minúsculas')
    else:
        print('É alfabético com maiúsculas e minúsculas')
elif algo.isalnum():
    print('É alfanumérico')
else:
    print('Não é alfabético nem numérico')