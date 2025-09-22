# FUNÇÕES DE REALIZAR UMA VENDA:
def cardapio(show= False):
    """
    Retorna ou exibe o dicionário de produtos do cardápio.

    Args:
        show (bool): Se True, exibe o cardápio formatado. Se False,
                     retorna o dicionário de produtos. Padrão é False.

    Returns:
        dict: O dicionário de produtos do cardápio, se 'show' for False.
              Exemplo: {'CATEGORIA': [['[1] Item', 10.00]]}
    """
    produtos = {'HAMBURGUERS': [['Big Py', 29.90],
                                ['PyChicken', 25.90], 
                                ['PyThree Bacon', 33.50],
                                ['Quartil Burguer', 29.90],
                                ['Cheedar PyMelt', 27.90],
                                ['PyThreese Burguer', 29.90] , 
                                ['CrisPy Bacon', 31.90]],
                'BEBIDAS': [['Refrigerante', 16.90],
                            ['Suco', 14.90], 
                            ['Água', 6.90], 
                            ['Milkshake', 19.90]],
                'ACOMPANHAMENTOS': [['Batata Frita', 14.90],
                                    ['Nurggets', 18.90]]}
    if show == True:
        index = 0
        for categoria, produtos in produtos.items():
            print(categoria)
            for p in produtos:
                print(f'[{index+1}] {p[0]}..........R${p[1]}')
                index += 1
            print(40*'-')
    if show == False:
        return produtos


def vender(*codigos):
    """
    Calcula o valor total de uma venda com base nos códigos dos itens.
    Se um código não for encontrado, ele é ignorado.

    Args:
        *codigos (int): Um ou mais códigos de itens do cardápio.

    Returns:
        float: O valor total da compra.
    """

    cardapio_itens = cardapio()
    todos_os_itens = []
    for categorias, produtos in cardapio_itens.items():
        for p in produtos:
            todos_os_itens.append(p)
    
    total_pagamento = 0
    itens_vendidos = []
    for codigo in codigos:
        try:
            item_detalhes = todos_os_itens[int(codigo)-1]
            total_pagamento += item_detalhes[1]
            itens_vendidos.append(item_detalhes)
        except IndexError:
            print(f'O código {codigo} não existe no cardápio')
 
    return total_pagamento, itens_vendidos


def relatorio(total_pagamento, itens_vendidos):
    """
    Gera e exibe um relatório detalhado da venda.

    Args:
        total (float): O valor total da venda.
        lista_itens (list): Uma lista de itens vendidos.
    """
    print(40*'-')
    print('Relatório de venda')
    print(40*'-')

    for i in itens_vendidos:
        print(f'{i[0]}..........R${i[1]:.2f}')
    print(f'Total: R$ {total_pagamento:.2f}')


# HEITOR -> FUNÇÃO MÉDIA DE PREÇO valor de cada um +/total

def pagar_como(metodos_pagamento, total_a_pagar):
    """
    Verificar qual forma de pagamento que o cliente deseja e calcular
    trocos em caso de pagamento em dinheiro.
    """
    print(10*'-', 'MÉTODOS DE PAGAMENTO', 10*'-')
    for idx, pagamento in enumerate(metodos_pagamento):
        print(f'[{idx+1}]..........{pagamento}')
    
    try:
        mp = int(input('Qual forma de pagamento? [1,2,3,4]:'))
        print(66*'-')

        if mp == 4:
            while True:
                try:
                    val_recebido = float(input(f'Valor recebido: R$ '))
                    troco = val_recebido - total_a_pagar
                    
                    if troco >= 0:
                        print(f'Troco: R$ {troco:.2f}')
                        break

                    else:
                        print(f'Valor insuficiente para pagamento. Faltam: R$ {-troco:.2f}.') 
                        op_insuficiente = input('Deseja inserir mais dinheiro? [S/N]: ').lower().strip()
                        if op_insuficiente == 'n':
                            print('Pagamento cancelado.')
                            return # Encerra a função
                        
                except ValueError:
                    print('Valor inválido. Por favor, digite um número.')
        print(f'Pagamento realizado via: {metodos_pagamento[mp-1]}')
    
        if mp not in [1, 2 ,3 ,4]:
            print('Código de pagamento inválido. Por favor, digite um código registrado.')
    
    except ValueError:
        print('Código de pagamento inválido. Por favor, digite um número inteiro.')