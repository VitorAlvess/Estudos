altura = float(input('Digite sua altura em Metros: '))
peso = float(input('Digite seu peso em KG: '))
imc = peso / (altura **2)

if imc < 18.5:
    print('Seu imc é {:.2f}, Você esta abaixo do peso'.format(imc))
elif imc <= 25:
    print('Seu imc é {:.2f}, Você esta no peso ideal'.format(imc))
elif imc <=30:
    print('Seu imc é {:.2f}, Você esta no sobrepeso'.format(imc))
elif imc <=40:
    print('Seu imc é {:.2f}. Você esta obeso'.format(imc))
else:
    print('seu imc é {:.2f}. Você é um obeso morbida'.format(imc))
