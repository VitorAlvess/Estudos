casa = float(input('Digite o valor da casa'))
anos = int(input('Digite em quantos anos você deseja pagar essa casa'))
salario = float(input('Digite o seu salario'))

prestacao = casa / ( anos * 12)


if prestacao > salario * 0.30:
    print('Você não pode financiar essa casa')
else:
    print('Você pode financiar essa casa')