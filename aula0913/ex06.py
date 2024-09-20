limite = int(input("insira um número inteiro: "))

if limite >= 100:
  n = 1
  soma = 0
  while n <= limite: 
    if n % 2 == 0: # otimização: inicializar {n} com 2 e só contar de 2 em 2
      soma += n
    n += 1

  print(f"a soma de todos os números pares entre 1 e {limite} é {soma}")
  # dica: usar o excel para testar valores altos
else:
  print("o valor deve ser no mínimo 100 !") # correção não tão obrigatória: não só terminar o programa, mas pedir o valor certo novamente
