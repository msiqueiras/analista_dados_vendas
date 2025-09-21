import pedido
import cadastros

print(20*'-', 'PYTHON BITES', 20*'-')
print('Sistema de gerenciamento')
operacoes_geral = {'Cadastro ou visualização de funcionário': 1,
            'Cadastrar ou visualização de cliente': 2,
            'Realizar venda': 3,
            'Calcular média de preço por produto': 4,
            'Gerar relatório da última venda': 5}
for op, cod in operacoes_geral.items():
    print(f'-> [{cod}]..........{op}')

funcionarios_empresa = []
clientes_empresa = []
sistema = True
while sistema:
        try:
            qual_op_geral = int(input('Digite um código GERAL de operação:'))

            if qual_op_geral == 1:
                cadastros.menu_cadastro_funcionario(funcionarios_empresa)

            if qual_op_geral == 2:
                cadastros.menu_cadastro_clientes(clientes_empresa)

            if qual_op_geral == 3:
                print(40*'-')
                print('CÁRDAPIO PYTHON BITES:')
                print(40*'-')
                pedido.cardapio(show = True)

                lista_pedidos = []
                pedido = True
                while pedido:
                    try:
                        itens_pedidos = int(input('Digite o código do item:'))
                        lista_pedidos.append(itens_pedidos)
                        continuar_pedido = str(input('Deseja continuar pedido? [S/N]')).lower().strip()
                        if continuar_pedido[0] == 'n':
                            pedido = False
                            print(40*'-')
                            print('PEDIDO FINALIZADO')
                            pagamento, itens_do_relatorio = pedido.vender(*lista_pedidos)
                            pedido.relatorio(pagamento, itens_do_relatorio)

                    except ValueError:
                         print('O código digitado não é um número inteiro.')
            

            continuar_operacoes = str(input('Deseja realizar outra operação? [S/N]')).lower().strip()
            if continuar_operacoes[0] == 'n':
                sistema = False
                print('PYTHON BITES ©')

        except ValueError:
            print(20*'-')
            print('Código não reconhecido.')
            print(20*'-')