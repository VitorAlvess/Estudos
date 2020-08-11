dezoito = cont = Mjoven = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo [M/F]').upper()

    if idade > 18:
        dezoito += 1
    if sexo == 'M':
        cont += 1
    if sexo =='F' and idade < 20:
        Mjoven += 1
    resposta = str(input('Quer continuar'))
    if resposta == 'N':
        break
print(f'{dezoito} tem mais de 18 anos')
print(f'O total de homens cadastrados é {cont}')
print(f'{Mjoven} tem menos de 20 anos')
