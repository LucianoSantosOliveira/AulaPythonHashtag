meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]
#seu código aqui

# Exercícios

## 1. Calculando % de uma lista

#Faremos algo parecido com "filtrar" uma lista. Mais pra frente no curso aprenderemos outras formas de fazer isso, mas com o nosso conhecimentoa atual já conseguimos resolver o desafio.

#Digamos que a gente tenha uma lista de vendedores e ao invés de saber todos os vendedores que bateram a meta, eu quero conseguir calcular o % de vendedores que bateram a meta. Ou seja, se temos 10 vendedores e 3 bateram a meta, temos 30% dos vendedores que bateram a meta.



numTotal = len(vendas)
numBateuMeta = 0
maiorVenda = 0
posMaior = 0

for i,venda in enumerate(vendas):
    if venda[1] > maiorVenda:
        maiorVenda = venda[1]
        posMaior = i
    if(venda[1]> meta):
        numBateuMeta += 1

print("Porcentagem foi:{:.2%}, Quem mais vendeu foi: {}, Valor: {}".format((numBateuMeta / numTotal),vendas[posMaior][0],maiorVenda))        