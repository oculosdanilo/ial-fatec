pares = 0

n = 0
while n < 5:
  x = float(input())

  if x % 2 == 0:
    pares += 1

  n += 1

print(f'{pares} valores pares')
