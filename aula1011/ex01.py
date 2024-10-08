lista = []

cont = 0
while cont < 10:
  lista.append(input(f"insira o {cont + 1}º valor: "))

  cont += 1

print("\nitens na lista: ")
for item in lista:
  print(item)
