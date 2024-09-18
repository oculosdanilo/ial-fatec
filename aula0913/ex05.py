n = 1
while n != 0:
  n = int(input("digite um número inteiro: "))

  if n % 2 == 0 and n % 5 == 0:
    print(f"{n} é divisível por 2 e 5")
  elif n % 2 == 0:
    print(f"{n} é divisível por 2")
  elif n % 5 == 0:
    print(f"{n} é divisível por 5")
