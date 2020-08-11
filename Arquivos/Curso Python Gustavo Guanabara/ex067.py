

while True:
    n1 = int(input('Quer ver a tabuada de qual valor?: '))
    if n1 < 0:
        break
    c = 1
    while c < 11:
        print(f'{n1} X {c} = {n1*c}')
        c += 1

print('Programa de tabuada encerrado. Volte sempre  ^-^')