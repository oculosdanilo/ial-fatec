from random import randint

lista = []

N = int(input("insira um número inteiro entre 0 e 50: "))

while N > 50 or N < 0:
  print("número inválido!\n")
  N = int(input("insira um número inteiro entre 0 e 50: "))

cont = 0
while cont < N:
  lista.append(randint(0, 1000))

  cont += 1

print("\nitens na lista: ")
for item in lista:
  print(item)
