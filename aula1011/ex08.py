N = int(input("insira quantos números devem ser requisitados: "))

while N < 0:
  print("número inválido! insira um número positivo ou zero")
  N = int(input("insira quantos números devem ser requisitados: "))

A = []
nA = 0
R = []
nR = 0

if N != 0:
  LMin = int(input("insira o número mínimo: "))
  LMax = int(input("insira o número máximo: "))

  if LMin > LMax:
    print("invertendo os números do intervalo...")
    LMinAntigo = LMin
    LMin = LMax
    LMax = LMinAntigo

  cont = 0
  while cont < N:
    E = int(input(f"insira o {cont + 1}º número inteiro para ser acrescentado: "))

    if LMin <= E <= LMax:
      A.append(E)
      nA += 1
    else:
      R.append(E)
      nR += 1
      print("número inserido fora do intervalo! rejeitado! (mas nunca esquecido...)")

    cont += 1

print(f'\n{nA} valor(es) na lista: {A}')
print(f'{nR} valor(es) rejeitados: {R}')
