from time import sleep

p1 = int(input('Digite o primeiro termo'))
r = int(input('Digite a razão'))
i = 0
print(p1, end=' -> ')
while i < 9:
    i = i + 1
    p1 = p1 + r
    print('{} '.format(p1), end='-> ')
print('PAUSA')
sleep(2)
print('=-'*20)
print('Você deseja continuar? ')
print('Digite o numero de termos a mais que você deseja')
print('Se não quiser nenhum Digite [0]')

c = int(input('Digite: '))
print('=-'*20)

if c == 0:
    print('Obrigado por usar o programa')
else:
    j = 0
    while j < c:
        j = j + 1
        p1 = p1 + r
        print('{} '.format(p1), end='-> ')
print('FIM')



