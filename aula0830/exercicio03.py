X = float(input("insira um numero: "))
Y = float(input("insira outro numero: "))

if X > Y:
  print(f'{X} é maior que {Y}')
elif Y > X:
  print(f'{Y} é maior que {X}')
else:
  print("os dois números são iguais")