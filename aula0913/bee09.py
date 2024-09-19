maior = 0
pos = 0
i = 0
while i < 100:
  x = int(input())

  if x > maior:
    maior = x
    pos = i + 1

  i += 1

print(maior)
print(pos)
