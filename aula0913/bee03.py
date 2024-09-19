positivos = 0
soma = 0
media = 0

n = 0
while n < 6:
  x = float(input())

  if x > 0:
    positivos += 1
    soma += x

  n += 1

media = soma / positivos
print(f'{positivos} valores positivos')
print(f'{media:.1f}')
