n = int(input())

cont = 0
while cont < n:
  x, y = map(int, input().split())
  soma = 0

  if x > y:
    contY = y + 1
    while contY < x:
      if contY % 2 != 0:
        soma += contY

      contY += 1

  elif y > x:
    contX = x + 1
    while contX < y:
      if contX % 2 != 0:
        soma += contX

      contX += 1

  print(soma)

  cont += 1