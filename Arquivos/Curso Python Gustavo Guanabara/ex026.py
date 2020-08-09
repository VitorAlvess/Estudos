n1 = str(input('digite o seu nome')).lower().strip()

print('O seu nome tem {} A'.format(n1.count('a')))
print(' A posição onde O A foi visto pela primeira vez é {}' .format(n1.find('a') + 1))
print('a ultima posição onde a foi visto é {} ' .format(n1.rfind('a') + 1))