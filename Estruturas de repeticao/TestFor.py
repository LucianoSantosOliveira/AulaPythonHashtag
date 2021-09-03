
from typing import Text


produtos = [
    "coca",
    "Pepsi",
    "Cavalo"             
]

texto = "Luciano"

print(len(produtos[0]))

for item in produtos:
    item += "Bebida "
    print(item)

for ch in texto:
    print(ch)

print(produtos)

vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
meta = 1000

totaldepessoa = len(vendas)
bateramMeta = 0
for item in vendas:
    if item > meta:
        bateramMeta = 1 + bateramMeta

print("Porcentagem que bateu meta: {:.2%}".format(bateramMeta / totaldepessoa ))