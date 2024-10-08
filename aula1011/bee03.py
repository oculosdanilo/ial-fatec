x, y = map(int, input().split())

while x != y:
  if x > y:
    print("Decrescente")
  elif y > x:
    print("Crescente")

  x, y = map(int, input().split())