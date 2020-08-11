print('-'*20)
print('LOJA TODOMUNDOVAI')
print('-'*20)
gasto = caro = menor = cont = 0
barato = ''




while True:
    nome = str(input('Produto: '))
    preco = float(input('Preço: '))
    resp = ' '
    cont += 1

    gasto += preco
    if preco > 1000:
        caro += 1
    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome


    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]

    if resp == 'N':
        break
print('-' *20)
print(f'O total gasto é {gasto}')
print(f' {caro} produtos custam mais de R$1000')

print(f'O produto mais barato é {barato} e custa {menor:.2f}')


