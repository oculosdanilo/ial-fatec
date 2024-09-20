n = 1
while n != 0:
  n = int(input("digite um número inteiro: "))

  if n % 2 == 0 and n % 3 == 0:
    print(f"{n} é divisível por 2 e 3")
  elif n % 2 == 0:
    print(f"{n} é divisível por 2")
  elif n % 3 == 0:
    print(f"{n} é divisível por 3")
