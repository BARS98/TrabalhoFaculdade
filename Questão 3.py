# ----------------Inicio dimensoesObjeto----------------
def dimensoesObjeto():
    volume = 0 #Contadores
    altura = 0
    comprimento = 0
    largura = 0

    while True:
        try:
            altura = int(input('Digite a altura do objeto(cm): '))
            comprimento = int(input('Digite a comprimento do objeto(cm): '))
            largura = int(input('Digite a largura do objeto(cm): '))
        except ValueError: #Se o usuario digitar qualquer caractere, acontece o except, o print e o loop volta ao começo
            print('Você digitou um valor não numérico\nPor favor digite as dimensões novamente')
            continue

        volume = altura * comprimento * largura #variavel criada para realizar o calculo do volume
        print('Volume do objeto(cm³): {:.1f}' .format(volume))
        if volume >= 0 and volume <= 1000: #Se o volume estiver em algum intervalo, ele retorna o valor
            return 10.00
        elif volume > 1000 and volume <= 10000:
            return 20.00
        elif volume > 10000 and volume <= 30000:
            return 30.00
        elif volume > 30000 and volume <= 100000:
            return 50.00
        else: #Se o volume estiver acima de 100000, ocorre o print e o loop volta ao inicio
            print('Não aceitamos objetos tão grandes\n Por favor digite as dimensões novamente')
# ------------------Fim dimensoesObjeto-----------------

# -------------------Inicio pesoObjeto------------------
def pesoObjeto():
    peso = 0 #Contador
    while True:
        try:
            peso = float(input('Digite o peso do objeto(kg):'))
        except ValueError:#Se o usuario digitar qualquer caractere, acontece o except, o print e o loop volta ao começo
            print('Você digitou um valor não numérico\nPor favor digite as dimensões novamente')
            continue

        print('Peso do objeto(kg): {}'.format(peso))
        if peso >= 0 and peso <= 0.1: #Se o peso estiver no intervalo, ele retorna o valor
            return 1
        elif peso >= 0.1 and peso <= 1:
            return 1.5
        elif peso >= 1 and peso <= 10:
            return 2
        elif peso >= 10 and peso <= 30:
            return 3
        else:#Se o peso estiver acima de 30, o print acontece e volta a pedir o peso
            print('Não aceitamos objetos tão pesados\n Por favor digite o peso novamente')

# ---------------------Fim pesoObjeto-------------------

# -------------------Inicio rotaObjeto------------------
def rotaObjeto():
    rota = 0 #Contador
    while True:
        try:
            rota = input('Selecione a rota desejada:\nRS - Rio de Janeiro para São Paulo\nSR - São Paulo para Rio de Janeiro\nBS - Brasília para São Paulo\nSB - São Paulo para Brasília\nBR - Brasília para Rio de Janeiro\nRB - Rio de Janeiro para Brasília\n>>> ')
        except ValueError:#Se o usuario digitar qualquer caractere, acontece o except, o print e o loop pede a rota novamente
            print('Você digitou um valor numérico\nPor favor digite a rota desejada novamente')
            continue
        if rota == 'RS':#Se o usuario digitou as siglas corretamente,retorna o valor
            return 1
        elif rota == 'SR':
            return 1
        elif rota == 'BS':
            return 1.2
        elif rota == 'SB':
            return 1.2
        elif rota == 'BR':
            return 1.5
        elif rota == 'RB':
            return 1.5
        else:#se o usuario digitou qualquer outro caracteres que nao sao estas siglas, acontece o print e loop pergunta a rota novamente
            print('Rota inexistente\n Por favor selecione a rota desejada novamente')



# --------------------Fim rotaObjeto--------------------


# Programa Principal
print('Bem-vindo a Breno Alves Rodrigues da Silva Logistica S.A.')
dimensoes = dimensoesObjeto()# os valores retornados em casa função estao nessas variaveis
peso = pesoObjeto()
rota = rotaObjeto()
print('Total á pagar(R$): {:.2F}'.format(dimensoes * peso * rota))#valor final vindo da equação