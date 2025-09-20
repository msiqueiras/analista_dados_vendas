import utilitarios as ut

ut.cardapio(show=True)
tupla = ut.vender(1, 10)

print('Com a função:', tupla)
lista = []
for x in tupla:
    lista.append(x)
print('Com a lista:', lista)

total = lista[0]
print(f'Total pagamento: R$ {total}')