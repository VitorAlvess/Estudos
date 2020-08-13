times = ('Athletico', 'Sport', 'Atletico-MG', 'Gremio', 'Internacional', 'Bragantino', 'Santos', 'Atletico-GO', 'Bahia',
         'Botafogo', 'Corinthias', 'Goias', 'Palmeiras', 'São paulo', 'Vasco da gama', 'Ceara', 'Coritiba', 'Flamengo', 'Fluminense',
         'Fortaleza')
print('-=' * 40)
print(f'A lista dos times brasileirão: {times}')
print('-=' * 40)
print(f'Os 5 primeiros colocados: {times[0:5]}')
print('-=' * 40)
print(f'Os 4 ultimos colocados: {times[-4:]}')
print('-=' * 40)
print(f'Em ordem Alfabetica; {sorted(times)}')
print('-=' * 40)
print(f'O são paulo esta na posição: {times.index("Palmeiras")+1}')