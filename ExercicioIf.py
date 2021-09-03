vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700
meta = 1000


#1. Cálculo de Bônus
#Crie um programa que calcule e dê um print no bônus que os funcionários devem receber segundo a regra:
#A meta é 1000 vendas.
#Se o valor de vendas for maior ou igual a meta, o valor do bônus do funcionário é 10% do valor de vendas.
#Caso contrário o valor de bônus do funcionário é 0.
#Print o bônus dos 3 funcionários

if vendas_funcionario1 >= 2000:
   print("Funcionario 1 bonus de 15%: {}".format(vendas_funcionario1*0.15))
elif vendas_funcionario1 >= 1000:
    print("Funcionario 1 bonus de 10%:{}".format(vendas_funcionario1*0.10))
else:
    print("Funcionario 1 sem bonus")

if(vendas_funcionario2)>=2000:
    print("Funcionario 2 bonus de 15% {}".format(vendas_funcionario2*0.15))
elif vendas_funcionario2 >=1000:
    print("Funcionario 2 com bonus de 10%{}".format(vendas_funcionario2*0.1))
else:
    print("Funcionario 2 sem bonus")    

if vendas_funcionario3 >= 2000:
    print("Funcionario 3 tem bonus de 15%: {}".format(vendas_funcionario3*0.15))
elif vendas_funcionario3 >=1000:
    print("Funcionario 3 com bonus de 10%: {}".format(vendas_funcionario3*0.10))        
