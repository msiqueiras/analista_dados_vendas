def cardapio(show= False):
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
    cardapio_itens = cardapio()
    itens = []
    tot_codigos = []
    for categorias, produtos in cardapio_itens.items():
        for produto in produtos:
            itens.append(produto)
    
    total_pagamento = 0
    for codigo in codigos:
        try:
            total_pagamento += itens[int(codigo)-1][1]
        except IndexError:
            print(f'O código {codigo} não existe no cardápio')
 
    return total_pagamento