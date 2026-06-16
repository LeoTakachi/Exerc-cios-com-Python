# Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. Os dados das vendas foram armazenados em um dicionário:
# {'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
#  'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
# Escreva um código que calcule o total de vendas e o produto mais vendido.

vendas_produtos = {'Produto A': 300
    , 'Produto B': 80
    , 'Produto C': 60
    ,'Produto D': 200
    , 'Produto E': 250
    , 'Produto F': 30}

total_vendas = 0
produto_mais_vendido = ''
unidades_produto_mais_vendido = 0
for produto in vendas_produtos.keys():
    total_vendas += vendas_produtos[produto]

    if vendas_produtos[produto] > unidades_produto_mais_vendido:
        unidades_produto_mais_vendido = vendas_produtos[produto]
        produto_mais_vendido = produto

print(f'Total de vendas: {total_vendas}')
print(f'Produto mais vendido: {produto_mais_vendido}')