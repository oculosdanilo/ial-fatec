limite = int(input("insira um número inteiro: "))

if limite >= 100:
  n = 1
  soma = 0
  while n <= limite:
    if n % 2 == 0:
      soma += n
    n += 1

  print(f"a soma de todos os números pares entre 1 e {limite} é {soma}")
else:
  print("o valor deve ser no mínimo 100 !")
