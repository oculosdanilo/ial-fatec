x = float(input("insira um número real: "))
lista = []

while x > 0:
  lista.append(x)

  x = float(input("insira um número real: "))

indice = 0
while indice < len(lista):
  print(f'{indice + 1}º número: {lista[indice]}')

  indice += 1
