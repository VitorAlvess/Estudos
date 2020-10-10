dados = []
cont = ''
mostrardados = 0
while True:
    jogador = {
        'nome': str(input('Nome:'))

    }
    gols = []
    tot = 0
    partidas = int(input('Partidas:'))
    for c in range(0, partidas):
        gols.append(int(input(f'Gols na {c + 1} partida: ')))
    jogador['gols'] = gols

    for c in range(len(gols)):
        tot = gols[c] + tot
    jogador['Total'] = tot
    dados.append(jogador.copy())
    jogador.clear()
    cont = str(input('Continuar: [S/N]')).upper()
    if cont == 'N':
        break
print(dados)
print('-' * 30)
print(f'{"COD":<}  {"NOME":<10} {"GOLS":^} {"Total":>18}')
for c in range(0, len(dados)):
    print(f'{c:<2}  {dados[c]["nome"] :<10} {dados[c]["gols"][:]} {dados[c]["Total"]:>18}  ')
while True:
    while True:
        mostrardados = int(input('Mostrar dados de qual jogador? [999 Para sair]:  '))
        if mostrardados > len(dados):
            print('Valor invalido Digite novamente')
            mostrardados = int(input('Mostrar dados de qual jogador? [999 Para sair]:  '))
        else:
            break

    if mostrardados == 999:
        break
    print(f'----Levantamento do jogador {dados[mostrardados]["nome"]}')
    for c in range(0, len(dados[mostrardados]["gols"])):
        print(f'        -No jogo {c+1} Fez {dados[mostrardados]["gols"][c]} Gol(s).')
print('Volte Sempre :)')
