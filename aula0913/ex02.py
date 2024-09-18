minimo = int(input("insira o valor mínimo inteiro: "))
maximo = int(input("insira o valor máximo inteiro: "))

if maximo > minimo:
  while minimo <= maximo:
    if minimo % 5 == 0:
      print(f'{minimo} é divisível por 5')

    minimo += 1
else:
  print("número máximo inválido!")
