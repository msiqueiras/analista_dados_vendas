import pedido
import cadastros
import inicializacao

print(20*'-', 'PYTHON BITES', 20*'-')

funcionarios_empresa = []
clientes_empresa = []
metodos_pagamento = ['pix', 'débito', 'crédito', 'dinheiro']
sistema = True
while sistema:
        inicializacao.limpar_tela()
        inicializacao.menu_principal()
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
                pedir = True
                while pedir:
                    try:
                        itens_pedidos = int(input('Digite o código do item:'))
                        lista_pedidos.append(itens_pedidos)
                        continuar_pedido = str(input('Deseja continuar pedido? [S/N]')).lower().strip()
                        if continuar_pedido[0] == 'n':
                            pedir = False
                            print(40*'-')
                            print('PEDIDO FINALIZADO')
                            total_a_pagar, itens_do_relatorio = pedido.vender(*lista_pedidos)
                            pedido.relatorio(total_a_pagar, itens_do_relatorio)
                            pedido.pagar_como(metodos_pagamento, total_a_pagar)
                            print('OBRIGADO E VOLTE SEMPRE!')
                            
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