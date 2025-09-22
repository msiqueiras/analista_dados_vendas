def menu_principal():
    """
    Exibir menu principal do sistema.
    """
    print('Sistema de gerenciamento')
    operacoes_geral = {'Cadastro ou visualização de funcionário': 1,
            'Cadastrar ou visualização de cliente': 2,
            'Realizar venda': 3,
            'Calcular média de preço por produto': 4,}
    for op, cod in operacoes_geral.items():
        print(f'-> [{cod}]..........{op}')

def limpar_tela():
    """
    Função para limpar a tela toda vez que outra operação dentro do sistema
    é realizada.
    """
    import os

    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')