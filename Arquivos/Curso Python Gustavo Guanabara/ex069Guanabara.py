while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0] # isso é importante o negocio do while
    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar? [S/N]')).strip().upper()[0]



