salario = float(input())

reajustePorcent = ""
reajusteValor = 0.0
novoSalario = 0.0
if 0 <= salario <= 400:
  reajustePorcent = "15 %"
  reajusteValor = salario * 0.15
elif 400 < salario <= 800:
  reajustePorcent = "12 %"
  reajusteValor = salario * 0.12
elif 800 < salario <= 1200:
  reajustePorcent = "10 %"
  reajusteValor = salario * 0.10
elif 1200 < salario <= 2000:
  reajustePorcent = "7 %"
  reajusteValor = salario * 0.07
else:
  reajustePorcent = "4 %"
  reajusteValor = salario * 0.04
novoSalario = salario + reajusteValor

print(f'Novo salario: {novoSalario:.2f}\nReajuste ganho: {reajusteValor:.2f}\nEm percentual: {reajustePorcent}')