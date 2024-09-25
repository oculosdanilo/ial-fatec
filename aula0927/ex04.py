i1 = 0
i2 = 0
lista1 = []
lista2 = []
listaFinal = []

while i1 < 10:
  x = int(input("insira um número inteiro p/ a primeira lista: "))
  lista1.append(x)

  i1 += 1

while i2 < 10:
  x = int(input("insira um número inteiro p/ a segunda lista: "))
  lista1.append(x)

  i2 += 1

listaFinal = lista1 + lista2
print(f'lista final: {listaFinal}')
