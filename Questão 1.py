print('Bem-vindo a loja do Breno Alves Rodrigues da Silva')
# Variáveis preco qtd usadas para receber o input do teclado
preco = float(input('Digite o valor do produto: '))
qtd = int(input('Digite a quantidade que deseja levar: '))
subtotal = preco * qtd

if 0 <= qtd <= 9:
    print('O valor sem desconto foi: R${:.2f}'.format(subtotal))
    print('O valor com desconto foi: R${:.2f}'.format(subtotal))  # desconto de 0%

elif qtd >= 10 and qtd <= 99:
    desconto = subtotal * 0.05
    preco_final = subtotal - desconto  # desconto de 5%
    print('O valor sem desconto foi: R${:.2f}'.format(subtotal))
    print('O valor com desconto foi: R${:.2f} (Desconto 5%)'.format(preco_final))

elif qtd >= 100 and qtd <= 999:
    desconto = subtotal * 0.10
    preco_final = subtotal - desconto  # desconto de 10%
    print('O valor sem desconto foi: R${:.2f}'.format(subtotal))
    print('O valor com desconto foi: R${:.2f} (Desconto 10%)'.format(preco_final))

else:
    desconto = subtotal * 0.15  # desconto de 15%
    preco_final = subtotal - desconto
    print('O valor sem desconto foi: R${:.2f}'.format(subtotal))
    print('O valor com desconto foi: R${:.2f} (Desconto15%)'.format(preco_final))

