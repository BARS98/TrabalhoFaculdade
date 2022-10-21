print('Bem-vindo a lanchonete do Breno Alves Rodrigues da Silva')
print('=' * 23,'Cárdapio','=' * 23)
print('| CÓDIGO |            DESCRIÇÃO            | VALOR(R$) |')
print('-'* 56)
print('|   100  |         Cachorro-Quente         |    9.00   |')
print('|   101  |      Cachorro-Quente Duplo      |   11.00   |')
print('|   102  |              X-Egg              |   12.00   |')
print('|   103  |             X-Salada            |   13.00   |')
print('|   104  |              X-Bacon            |   14.00   |')
print('|   105  |               X-Tudo            |   17.00   |')
print('|   200  |         Refrigerante Lata       |    5.00   |')
print('|   201  |           Chá Gelado            |    4.00   |')
soma = 0
while True:
     codigo = int(input('Entre com o código desejado: '))
     # cachorro quente
     if codigo == 100:
            soma+=9.00
     # cachorro quente duplo
     elif codigo == 101:
            soma+= 11.00
     # x-egg
     elif codigo == 102:
        soma+= 12.00
     # x-salada
     elif codigo == 103:
        soma+= 13.00
     # x-bacon
     elif codigo == 104:
        soma+= 14.00
     # x-tudo
     elif codigo == 105:
        soma+= 17.00
     # refrigerante
     elif codigo == 200:
        soma+= 5.00
     # cha gelado
     elif codigo == 201:
        soma+= 4.00
     else: # se digitar algum digito que nao esteja na tabela, ocorre o print
        print('Opção inválida\nTente novamente')
        continue
    # caso cliente queira outro lanche, acontece esse codigo
     repetir = input('Deseja pedir mais alguma coisa?(S/N)')
     if repetir == 'S':
      continue
    # caso nao, o programa acaba e mostra o subtotal da compra
     elif repetir == 'N':
        (print('Valor à pagar: {:.2f}'.format(soma)))
        break

