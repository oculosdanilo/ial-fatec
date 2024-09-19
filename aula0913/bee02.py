positivos = 0

n = 0
while n < 6:
  x = float(input())

  if x > 0:
    positivos += 1

  n += 1

print(f'{positivos} valores positivos')
