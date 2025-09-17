def cardapio():
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

    for key, value in produtos.items():
        print(key)
        for v in value:
            print(f'{v[0]}..........R${v[1]}')
        print(40*'-')