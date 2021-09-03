meta = 10000
vendas = [
    ('João', 15000),
    ('Julia', 27000),
    ('Marcus', 9900),
    ('Maria', 3750),
    ('Ana', 10300),
    ('Alon', 7870),
]



for nome, venda in vendas:
    if venda > meta:
        print("{},Vendeu:{}".format(nome,venda))


print("--------------------------------------------------------------------")     



vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604), ('máquina de café', 718654, 867660), ('kindle', 531580, 78830), ('geladeira', 973139, 710331), ('adega', 892292, 646016), ('notebook dell', 422760, 694913), ('notebook hp', 154753, 539704), ('notebook asus', 887061, 324831), ('microsoft surface', 438508, 667179), ('webcam', 237467, 295633), ('caixa de som', 489705, 725316), ('microfone', 328311, 644622), ('câmera canon', 591120, 994303)]

for venda in vendas_produtos:

    nome , venda2019 , venda2020 = venda
    if venda2020 > venda2019:
        #print("-------------------------")
        print("{},Venda 2019: {}, Venda 2020: {}, Porcentagem de crescimento: {:.2%}".format(nome,venda2019,venda2020, (venda2020 / venda2019 - 1)))
        #print("Vendeu mais em 2020: {}".format(nome))