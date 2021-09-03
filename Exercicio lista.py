
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

totalVendas = vendas_1sem + vendas_2sem


print("O melhor mes foi: {0}, com valor de: {1}"
.format(meses[totalVendas.index(max(totalVendas))],max(totalVendas)))

print("O pior mes foi: {0}, com valor de: {1}"
.format(meses[totalVendas.index(min(totalVendas))], min(totalVendas)))

print("Faturamento total do ano: {0}"
.format(sum(totalVendas)))

porcent =  max(totalVendas)/sum(totalVendas) 
print("O mes que mais vendeu representou: {:.2%} por cento"
.format(porcent))

totalVendas.sort(reverse=True)
print(totalVendas[:3])


