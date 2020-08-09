from datetime import date
data = date.today().year
nasci = int(input('Digite sua data de nascimento'))

idade = data - nasci

if idade == 18:
    print('Você tem 18 anos, é hora de se alistar')
elif idade > 18:
    print('Você ja passou do tempo do alistamento, ja faz {} anos'.format(idade - 18))
else:
    print('Você ira se alistar em {} ano(s)'.format(18 - idade))
