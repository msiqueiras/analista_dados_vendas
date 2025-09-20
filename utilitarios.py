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
    produtos = {'HAMBURGUERS': [['[1] Big Py', 29.90],
                                ['[2] PyChicken', 25.90], 
                                ['[3] PyThree Bacon', 33.50],
                                ['[4] Quartil Burguer', 29.90],
                                ['[5] Cheedar PyMelt', 27.90],
                                ['[6] PyThreese Burguer', 29.90] , 
                                ['[7] CrisPy Bacon', 31.90]],
                'BEBIDAS': [['[8] Refrigerante', 16.90],
                            ['[9] Suco', 14.90], 
                            ['[10] Água', 6.90], 
                            ['[11] Milkshake', 19.90]],
                'ACOMPANHAMENTOS': [['[12] Batata Frita', 14.90],
                                    ['[13] Nurggets', 18.90]]}
    if show == True:
        for categoria, produtos in produtos.items():
            print(categoria)
            for p in produtos:
                print(f'{p[0]}..........R${p[1]}')
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
    tot_codigos = []
    for categorias, produtos in cardapio_itens.items():
        for produto in produtos:
            todos_os_itens.append(produto)
    
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
    print(f'Total: R$ {total_pagamento}')


