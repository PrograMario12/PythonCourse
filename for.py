maximo = 100
valores = [10,20,50.5,9.8,10]
tmp = 0

for valor in valores:
    print(valor)
    tmp += valor

print(tmp)

if tmp > maximo:
    print("Se supera el máximo")
else:
    print("No se supera")