def calcular_medias(produtos):
    total_geral = 0
    qtd_geral = 0

    medias_categorias = {}

    for categoria, itens in produtos.items():
        total_categoria = 0
        qtd_categoria = 0

        for item in itens:
            preco = item[1]
            total_categoria += preco
            qtd_categoria += 1
            total_geral += preco
            qtd_geral += 1

        media_categoria = total_categoria / qtd_categoria
        medias_categorias[categoria] = media_categoria

    media_geral = total_geral / qtd_geral

    return media_geral, medias_categorias
media_geral, medias_categorias = calcular_medias(produtos)

# Exibindo os resultados
#print(f" Média geral dos produtos: R$ {media_geral:.2f}\n")

#print(" Média por categoria:")
#for categoria, media in medias_categorias.items():
#    print(f" - {categoria}: R$ {media:.2f}")
