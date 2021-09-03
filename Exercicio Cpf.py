
cpf = input("Digite seu CPF")

cpf = cpf.strip()
cpf = cpf.replace(".","").replace("-","")


if(len(cpf) >= 11 and cpf.isnumeric()):
    print(cpf)
else:
    print("Cpf errado")    