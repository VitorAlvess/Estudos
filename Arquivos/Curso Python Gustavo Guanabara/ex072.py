numeros = ('Zero', 'Um', 'Dois', 'Tres', 'Quadro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
           'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito' , 'Dezenove', 'Vinte')

n1 = ' '
while n1 not in range(0, 21):
    n1 = int(input('Digite um numero entre 0 e 20: '))
print(numeros[n1])
