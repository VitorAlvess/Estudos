n1 = c = soma = 0



while True:
    n1 = int(input('Digite um valor (999 para parar): '))
    if n1 == 999:
        break
    soma += n1
    c += 1
print(f'Foram digitados {c} numeros e a soma deles é = {soma}!')
