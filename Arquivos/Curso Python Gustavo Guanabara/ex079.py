valores = []
c = 0
while True:
    v = int(input('Digite um valor: '))
    if v in valores:
        print('Valor Duplicado')

    if v not in valores: #bugo demais com o in slk
        valores.append(v)
        print('Valor adcionado com suceeso')

    escolha = input('Quer continuar?[S/N] :').upper().strip()[0]
    while escolha not in 'SN':
        escolha[0] = input('Digite novamente')
    c += 1
    if escolha == 'N':
        break

print(f'Você digitou os valores {sorted(valores)}')