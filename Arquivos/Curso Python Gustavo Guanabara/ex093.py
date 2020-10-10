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
print('-' * 40)
print(jogador)
print('-' * 40)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-' * 40)
print(f'O jogador {jogador["nome"]} jogou {partidas} Partidas.')
for c in range(0, partidas):
    print(f'     Na partida {c+1}, fez {gols[c]} Gols ')
print(f'     Foi um total de {jogador["Total"]} Gols')
