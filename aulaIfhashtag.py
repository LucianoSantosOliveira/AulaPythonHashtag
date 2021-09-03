#Analisar bonus dos funcionarios
meta = 20000.00

vendido = float(input("Total vendido: "))

if vendido >= (meta * 2):
    print("7 de bonus:{}".format(vendido * 0.07))

elif vendido >= meta:
    print("3 de bonus{}".format(vendido * 0.03))
else:
    print("Nao há bonus")    
