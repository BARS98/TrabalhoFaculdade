lista_pecas = [] #lista das peças


# --------------------cadastrarPeca--------------------------
def cadastrarpeca(codigo_peca):
    print('CADASTRO DE PEÇA ')
    print('A peça foi cadastrada pelo código {}'.format(codigo_peca))
    nome = input('Insira o nome da peça: ')
    fabricante = input('Insira o fabricante da peça: ')
    valor = float(input('Insira o valor da peça'))
    dicionario_pecas = {'codigo': codigo_peca, 'nome': nome, 'fabricante': fabricante, 'valor': valor} #dicionario com as chaves e valores
    lista_pecas.append(dicionario_pecas.copy())#a lista lista_pecas copia as informaçoes no dicionario


# -----------------------------FIM----------------------------

# -----------------------consultarPeca----------------------
def consultarPeca():
    print('CONSULTAR PEÇAS')
    while True:
        try:
            menu_consultar = int(input(
                'O que deseja consultar?\n 1 - Consultar todas as peças\n 2 - Consultar por Código\n 3 - Consultar '
                'por Fabricante\n 4 - Retornar\n >>>'))
            if menu_consultar == 1:
                print('CONSULTAR TODAS')
                for peca in lista_pecas:  #o loop seleciona cada dicionario e coloca na lista
                    for key, value in peca.items():  #ai ele seleciona cada conjunto de chave e valor e imprime na tela
                        print('{} : {}'.format(key, value))
                        print()

            elif menu_consultar == 2:
                print('CONSULTAR CÓDIGO')
                entrada_codigo = int(input('Insira o código: '))
                for peca in lista_pecas:
                    if (peca['codigo'] == entrada_codigo):#o if checa se existe o codigo no dicionario, se tiver ele imprime
                        for key, value in peca.items():
                            print('{} : {}'.format(key, value))
                            print()

            elif menu_consultar == 3:
                print('CONSULTAR FABRICANTE')
                entrada_fabricante = input('Insira o fabricante: ')
                for peca in lista_pecas:
                    if (peca['fabricante'] == entrada_fabricante):#o if checa se existe o fabricante no dicionario
                        for key, value in peca.items():
                            print('{} : {}'.format(key, value))
                            print()

            elif menu_consultar == 4:
                return#se o usuario digitar 4, ele volta ao começo do loop
            else:
                print('Opção inválida\n Digite uma das opções acima')
                continue
        except ValueError:
            print('Digite somente valores numéricos inteiros')
            continue


# -----------------------------FIM ---------------------------------

# ---------------------------removerPeca-----------------------------
def removerPeca():
    print('REMOVER PEÇAS')
    entrada_remover = int(input('Insira o código: '))
    for peca in lista_pecas:
        if (peca['codigo'] == entrada_remover):# para poder remover a peça, eh necessario do codigo dela
            lista_pecas.remove(peca)
            print('Estudante removido')
            return


# -----------------------------FIM-----------------------------------


# PROGRAMA PRINCIPAL
print('Bem-vindo ao programa de conttrole de estoque do Breno Alves Rodrigues da Silva')
codigo_peca = 0 #variavel contador para registrar as peças
while True:
    try:
        menu = int(input(
            'Digite a opção desejada:\n 1 - Cadastrar Peça\n 2 - Consultar Peça\n 3 - Remover Peça\n 4 - Sair\n >>>'))
        if menu == 1:
            codigo_peca += 1# se o usuario for cadastrar a peça, o contador ja registra ela antes de chegar na função
            cadastrarpeca(codigo_peca)#vai para a função de cadastro
        elif menu == 2:
            consultarPeca()#vai para a função de consulta
        elif menu == 3:
            removerPeca()#vai para a função de remoção
        elif menu == 4:
            print('Encerrando o programa...')
            break#se o usuario digitar 4, o programa finaliza
        else:
            print('Escolha apenas as opções disponiveis acima')
            continue
    except ValueError:
        print('Erro!\nPor favor digite apenas valores numéricos inteiros')
