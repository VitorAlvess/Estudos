media = 0
maior = 0
velho = ''
menos = 0


for c in range(1, 5):
    nome = input('Digite o nome da pesssoa {}: '.format(c))
    idade = int(input('Digite a idade da pessoa {}: '.format(c)))
    sexo = input('Digite o sexo da pessoa {} (H ou M): '.format(c)).upper()
    media = media + idade

    if sexo == 'H' and idade > maior:
        maior = idade
        velho = nome

    if sexo == 'M' and idade < 20:
        menos = menos + 1



print('A media de idade do grupo é {} anos'.format(media/4))
print('A homem mais velho é {} com {} anos'.format(velho, maior))
print('A {} mulheres que possuem menos de 20 anos'.format(menos))
