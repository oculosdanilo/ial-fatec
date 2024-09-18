n = int(input("insira um número inteiro: "))

x = 2
primo = True
while primo and x < n:
  primo = n % x != 0

  x += 1

if primo:
  print(f"{n} é um número primo")
else:
  print(f"{n} não é um número primo")
