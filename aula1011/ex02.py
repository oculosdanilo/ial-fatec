lista = []
listaInvertida = []

cont = 0
while cont < 10:
  lista.append(input(f"insira o {cont + 1}º valor: "))

  cont += 1

contI = 9
while contI >= 0:
  listaInvertida.append(lista[contI])

  contI -= 1

print("\nitens na lista invertida: ")
for item in listaInvertida:
  print(item)
