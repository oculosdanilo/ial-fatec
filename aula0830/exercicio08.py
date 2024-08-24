Lado1 = float(input("insira o primeiro lado do triangulo: "))
Lado2 = float(input("insira o segundo lado do triangulo: "))
Lado3 = float(input("insira o terceiro lado do triangulo: "))

if ((Lado1 < Lado3 and Lado2 < Lado3 and Lado1 + Lado2 > Lado3) or (
    Lado1 < Lado2 and Lado3 < Lado2 and Lado1 + Lado3 > Lado2) or (
    Lado2 < Lado1 and Lado3 < Lado1 and Lado2 + Lado3 > Lado1) or
    Lado1 == Lado2 == Lado3):

  if Lado1 != Lado2 and Lado1 != Lado3 and Lado2 != Lado3:
    print("o triângulo é escaleno")
  elif Lado1 == Lado2 == Lado3:
    print("o triângulo é equilátero")
  else:
    print("o triângulo é isósceles")

else:
  print("os lados não formam um triângulo")