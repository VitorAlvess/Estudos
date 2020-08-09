vel = float(input('Digite a velocidade do carro: '))

if vel > 80:
    n1 = vel - 80
    print('Vc foi mutado no valor de {}' .format(n1 * 7))
else:
    print('não foi mutado')