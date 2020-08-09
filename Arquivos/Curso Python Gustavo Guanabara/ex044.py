preco = float(input('Digite o preço: '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] a vista no dinheiro/cheque')
print('[ 2 ] a vista no cartão')
print('[ 3 ] parcelado em 2x no cartão')
print('[ 4 ] parcelado em 3x ou mais no cartao')
opc = int(input('Digite o numero da opção: '))

if opc == 1:
    print('O valor de {} vai para {} com 10% de desconto'.format(preco, preco - (preco * 0.10)))

elif opc == 2:
    print('O valor de {} vai para {} com 5% de desconto'.format(preco, preco - (preco * 0.05)))

elif opc == 3:
    print('O valor de {} em parcela de 2x fica em {}'.format(preco, preco / 2))

elif opc == 4:
    juros = preco + (preco * 0.20)
    parcela = int(input('Digite a quantidade de parcelas'))
    print('O valor de {} vai para {} com 20% de juros e as parcelas de {:.2f}'.format(preco,juros, juros / parcela))


else:
    print('A opção {} não é uma opção disponivel'.format(opc))
