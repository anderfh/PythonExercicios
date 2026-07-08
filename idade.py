from datetime import date
def idade(dataNascimento):
    data = dataNascimento.split('/')
    datanasc = date(int(data[2]), int(data[1]), int(data[0]))
    hoje = date.today()
    idade = (hoje.year - datanasc.year)
    if (datanasc.month, datanasc.day) >= (hoje.month, hoje.day):
        idade -= 1
    return idade
