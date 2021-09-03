meta = 10000.0
vendas = [
    ['João', 15000.00],
    ['Julia', 27000.00],
    ['Marcus', 9900.00],
    ['Maria', 3750.00],
    ['Ana', 10300.00],
    ['Alon', 7870.00],
]
#seu código aqui



for i,venda in enumerate(vendas):
    if(venda[1] > meta):
        print("O vendedor {} bateu a meta com {} vendas".format(venda[0], venda[1]))