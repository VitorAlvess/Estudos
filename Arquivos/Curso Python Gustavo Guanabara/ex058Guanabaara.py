from random import randint
n1 = 0
n2 = randint(1, 10)
i = 0
print('Pensei em um numero de 1 a 10, Tente adivinhar :3')
while n1 != n2:
    n1 = int(input('Qual é o seu palpite?'))
    if n2 > n1:
        print('Mais um pouco')
    if n2 < n1:
        print('Um pouco Menos')


    i += 1
print('=-' * 20)
print('Você acertou :)')
print('Foram necessaria(s) {} tentativas'.format(i))
print('-=' * 20)


