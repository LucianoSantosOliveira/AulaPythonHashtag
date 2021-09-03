vendas = []

i =0 
produto = "a"
while True:
    

    produto = input("Qual o produto?")
    if not produto:
        break
    qdt = int(input("Quantidade?"))
    vendas.append([produto ,qdt])
    i += 1

print (vendas)
