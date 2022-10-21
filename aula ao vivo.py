listaEstudantes = []


# --------------------COMEÇO cadastrarEstudante-----------------
def cadastrarEstudante(ru):
    print('Bem-vindo ao cadastro estudantes')
    print('O RU do estudante a ser cadastrado é {}'.format(ru))
    nome = input('Digite o nome do estudante: ')
    turma = input('Digite a turma do estudante: ')
    dicionarioEstudante = {'ru': ru, 'nome': nome, 'turma': turma}
    listaEstudantes.append(dicionarioEstudante.copy)


# --------------------FIM cadastrarEstudante--------------------

# --------------------COMEÇO consultarEstudante-----------------
def consultarEstudante():
    print('Bem-vindo ao consultar estudantes')
    while True:
        try:
            opConsultar = int(input(
                'O que deseja consultar?\n 1 - Consultar todos os estudantes\n 2 - Consultar por RU\n 3 - Consultar por Turma\n 4 - Retornar\n >>>'))
            if opConsultar == 1:
                print('Bem-vindo a consultar TODOS')
                for estudante in listaEstudantes:
                    for key, value in estudante.items():
                        print('{} : {}'.format(key, value))
            elif opConsultar == 2:
                print('Bem-vindo a consultar por RU')


            elif opConsultar == 3:
                print('Bem-vindo a consultar por TURMA')


            elif opConsultar == 4:
                return


            else:
                print('Opção inválida\n Digite uma das opções acima')
                continue
        except ValueError:
            print('Digite somente valores numéricos inteiros')
            continue


# --------------------FIM cadastrarEstudante---------------------

# --------------------COMEÇO removerEstudante--------------------
def removerEstudante():
    print('Bem-vindo ao remover estudantes')


# --------------------FIM renoverEstudante-----------------------

# --------------------COMEÇO MAIN--------------------------------
print('Bem-vindo ao programa de controle de estudantes breno')
registroAcademico = 0
while True:
    try:
        opcao = int(input(
            'Digite a opção desejada:\n 1 - Cadastrar Estudante\n 2 - Consultar Estudantes\n 3 - Remover Estudante\n 4 - Sair\n >>>'))
        if opcao == 1:
            registroAcademico += 1
            cadastrarEstudante(registroAcademico)
        elif opcao == 2:
            consultarEstudante()
        elif opcao == 3:
            removerEstudante()
        elif opcao == 4:
            print('Encerrando o programa...')
            break
        else:
            print('Escolha apenas as opções disponiveis acima')
            continue
    except ValueError:
        print('Erro!\nPor favor digite apenas valores numéricos inteiros')

# --------------------FIM MAIN-----------------------------------
