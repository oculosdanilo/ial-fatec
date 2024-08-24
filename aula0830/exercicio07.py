A = float(input('insira o numero A: '))
B = float(input('insira o numero B: '))
C = float(input('insira o numero C: '))

Delta = B ** 2 - (4 * A * C)
Raiz1 = (-B + (Delta ** 0.5)) / (2 * A)
Raiz2 = (-B - (Delta ** 0.5)) / (2 * A)

print(f'a equação é {A}x² + {B}x + {C} = 0')
print(f'o delta é: {Delta}')
if B ** 2 - (4 * A * C) > 0:
  print(f'as raizes são: x1 = {Raiz1} e x2 = {Raiz2}')
elif B ** 2 - (4 * A * C) == 0.0:
  print(f'a única raiz é: x1 = {Raiz1}')
else:
  print('o delta é negativo (não há raízes reais)')
