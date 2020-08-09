from datetime import date

ano = date.today().year


i = 1
cont = 0
for c in range(1, 8):
    n1 = int(input('Digite a data de nascimento da pessoa {}: '.format(i)))
    vl = ano - n1
    i = i + 1
    if vl < 21:
        cont = cont + 1
print('{} pessoas ja atingiram a maior idade e {} pessoas não atingiram a maior idade'.format(7 - cont, cont))

