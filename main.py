import utilitarios as ut

print(10*'-', 'PYTHON BITES', 10*'-')
print('Sistema de gerenciamento')
operacoes = {'Cadastrar vendedor, cliente ou produto': 1,
             'Realizar venda': 2,
             'Calcular média de preço por produto': 3,
             'Gerar relatório da última venda': 4}
for op, cod in operacoes.items():
    print(f'-> [{cod}]..........{op}')