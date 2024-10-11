LMin = int(input("insira o número mínimo: "))
LMax = int(input("insira o número máximo: "))

A = []
nA = 0

if LMin > LMax:
  LMinAntigo = LMin
  LMin = LMax
  LMax = LMinAntigo

cont = 0         # pode ser também: 
while cont < 10: # for cont in range(10)
  N = int(input(f"insira o {cont + 1}º número inteiro para ser acrescentado: "))

  if LMin <= N <= LMax:
    A.append(N)
    nA += 1
  else:
    print("número inserido fora do intervalo! ignorando...")

  cont += 1

print(f'\n{nA} valor(es) na lista: {A}')
