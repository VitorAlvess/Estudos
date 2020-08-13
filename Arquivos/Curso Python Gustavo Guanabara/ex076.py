produtos = ('lapis', 1.40, 'Frango', 50.00, 'Estojo', 40.00, 'Mochila', 50)
print('=-' * 20)
print(f'{"ATACA O ADÂO":^35} ')
print('=-' * 20)
for c in range(len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<20}', end='')
    else:
        print(f'R$ {produtos[c]:>.2f}')
print('=-' * 20)

