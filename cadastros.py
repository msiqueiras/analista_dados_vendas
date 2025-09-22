def cadastrar_funcionario(lista_funcionarios):
    """
    Coleta dados do usuário e adiciona um novo funcionário à lista
    """
    from random import randint
    print(10*'-', 'CADASTRO DE FUNCIONÁRIO', 10*'-')
    id_funcionario = randint(1_000_000, 9_999_999)
    nome_completo = str(input('Nome completo:')).title().strip()
    cargo = str(input('Cargo:')).title().strip()
    
    dados_funcionario = {'Nome completo': nome_completo,
                        'ID': id_funcionario,
                        'Cargo': cargo }
    lista_funcionarios.append(dados_funcionario)
    print("Funcionário cadastrado com sucesso!")
    
    print(20*'-', 'Informações do registro:', 20*'-')
    for class_infos, info in dados_funcionario.items():
        print(f'{class_infos}.....{info}')
    print(66*'-')


def visualizar_funcionarios(lista_funcionarios):
    """
    Exibe todos os funcionários cadastrados na lista
    """
    print(10*'-', 'VISUALIZAÇÃO DA LISTA DE FUNCIONÁRIOS', 10*'-')
    if lista_funcionarios:
        for idx, funcionario in enumerate(lista_funcionarios):
            print(f'Funcionário {idx+1}')
            for class_infos, info in funcionario.items():
                print(f'{class_infos}.....{info}')
            print(66*'-')
    else:
        print('Lista de funcionários vazia.')


def menu_cadastro_funcionario(lista_funcionarios):
    """
    Exibe o menu de opções de funcionário
    """
    print(40*'-')
    print('CADASTRO OU VISUALIZAÇÃO DE FUNCIONÁRIOS:')
    print(40*'-')
    print('-> [1].......... Cadastrar funcionário')
    print('-> [2].......... Visualização de funcioários')
    
    try:
        qual_op_cf = int(input('Digite o código da operação:'))

        if qual_op_cf == 1:
            cadastrar_funcionario(lista_funcionarios)
        elif qual_op_cf == 2:
            visualizar_funcionarios(lista_funcionarios)
        else:
            print("Código de operação inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")


def cadastrar_cliente(lista_clientes):
    """
    Cadastrar novos clientes
    """
    print(10*'-', 'CADASTRO DE CLIENTES', 10*'-')
    nome_completo = str(input('Nome completo:'))
    cpf_errado = True
    while cpf_errado:
        try:
            cpf = int(input('CPF:'))
            cpf_errado = False
        except ValueError:
            print('CPF DIGITADO INVÁLIDO. Por favor, digite apenas números')
    dados_cliente = {'Nome completo': nome_completo,
                     'CPF': cpf}
    lista_clientes.append(dados_cliente)


def visualizar_clientes(lista_clientes):
    """
    Exibir a lista de todos os clientes registrados
    """
    print(10*'-', 'VISUALIZAÇÃO DA LISTA DE CLIENTES', 10*'-')
    if lista_clientes:
        for idx, cliente in enumerate(lista_clientes):
            print(f'Cliente {idx+1}')
            for class_infos, info in cliente.items():
                print(f'{class_infos}.....{info}')
            print(66*'-')
    else:
        print('Lista de clientes vazia.')


def  menu_cadastro_clientes(lista_clientes):
    """
    Exibe o menu de opções de clientes
    """
    print(40*'-')
    print('CADASTRO OU VISUALIZAÇÃO DE CLIENTES:')
    print(40*'-')
    print('-> [1].......... Cadastrar cliente')
    print('-> [2].......... Visualização de clientes')
    
    try:
        qual_op_cf = int(input('Digite o código da operação:'))

        if qual_op_cf == 1:
            cadastrar_cliente(lista_clientes)
        elif qual_op_cf == 2:
            visualizar_clientes(lista_clientes)
        else:
            print("Código de operação inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")