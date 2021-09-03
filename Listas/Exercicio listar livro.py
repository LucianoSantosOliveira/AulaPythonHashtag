


from typing import cast


produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 'ar condicionado', 'alexa', 'máquina de café', 'kindle']

#cada item da lista dos produtos corresponde a quantidade de vendas no mês e preço, nessa ordem
produtos_ecommerce = [
    [10000, 2500],
    [50000, 40],
    [7000, 1200],
    [20000, 1500],
    [5800, 1300],
    [7200, 2500],
    [200, 800],
    [3300, 700],
    [1900, 400]
]

print("Lucro antes do imposto: {:,}".format(produtos_ecommerce[produtos.index("livro")][0] * produtos_ecommerce[produtos.index("livro")][1]))
antigo = produtos_ecommerce[produtos.index("livro")][0] * produtos_ecommerce[produtos.index("livro")][1]

try:
    produtos_ecommerce[produtos.index("livro")][1] += produtos_ecommerce[produtos.index("livro")][1] * 0.10 
except:
    print(Exception)
    print("Não ha livros na lista") 

novo = produtos_ecommerce[produtos.index("livro")][0] * produtos_ecommerce[produtos.index("livro")][1]
print("Lucro depois do imposto: {:,}".format(produtos_ecommerce[produtos.index("livro")][0] * produtos_ecommerce[produtos.index("livro")][1]))
print("Pagamos:{:,}".format(novo - antigo))
print(produtos_ecommerce[produtos.index("livro")][1])        