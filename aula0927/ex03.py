i = 0
lista = []
while i < 10:
  x = input("insira um valor: ")
  lista.append(x)

  i += 1

lista.reverse()
print(f'lista inversa: {lista}')
