sal = float(input('Digite o valor do salario'))

if sal > 1250:
    au = sal + ( sal * 0.10)
    print('O seu salario com um aumento de 10% é R$ {} '.format(au))
else:
    au = sal + (sal * 0.15)
    print('O seu novo salario com um aumento de 15 é R$ {}'.format(au))