


coca = "BEB1300543"
pepsi = "BEB1300545"
vinhoprimit = "BAC1546001"
vodksmirnoff ="BAC17675002" 


bebida = input("Codigo da bebida")

print("BAC" in bebida)






qtdeCoca = 150
qtdePespi = 130
precoCoca = 1.50
precoPepsi = 1.50
custoLoja=2500


print(qtdeCoca * precoCoca)
print(qtdePespi * precoPepsi)

faturamento = ((qtdeCoca * precoCoca) + (qtdePespi * precoPepsi)) - custoLoja

#bac
# print(faturamento)
print("Teste do format {}".format(((qtdeCoca * precoCoca) + (qtdePespi * precoPepsi)) - custoLoja))