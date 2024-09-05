somaNeg = 0
somaPos = 0
X = 1
while X != 0:
  X = int(input("digite um valor negativo, positivo ou zero: "))
  if X != 0:
    if X > 0:
      somaPos += X
    if X < 0:
      somaNeg += X

print(f'total dos positivos: {somaPos}')
print(f'total dos negativos: {somaNeg}')