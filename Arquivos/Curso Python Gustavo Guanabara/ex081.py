valores = []
while True:
    valores.append(int(input('Digite um valor')))
    con = input('Deseja continuar [s/n]').upper()
    if con == 'N':
        break
print(f'A quantidade de numeros digitados é {len(valores)} numeros ')
print(f'A ordem dos numeros decrescente é = {sorted(valores, reverse=True)}')
if 5 in valores:
    print('tem o numero 5 na lista')
else:
    print('O valor 5 não esta na lista')