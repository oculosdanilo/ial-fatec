salario = float(input())

if salario <= 2000:
  print("Isento")
else:
  imposto = 0.0
  if 2000 < salario <= 3000:
    imposto = (salario - 2000) * 0.08
  elif 3000 < salario <= 4500:
    imposto = ((salario - 3000) * 0.18) + (((salario - 2000) * 0.08) - ((salario - 3000) * 0.08))
  else:
    imposto = ((salario - 4500) * 0.28) + (((salario - 3000) * 0.18) - ((salario - 4500) * 0.18)) + (
        ((salario - 2000) * 0.08) - ((salario - 3000) * 0.08))
  print(f"R$ {imposto:.2f}")
