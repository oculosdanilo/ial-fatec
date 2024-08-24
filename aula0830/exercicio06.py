Nome = input("insira o nome do(a) lutador(a): ")
Peso = float(input("insira o peso dele(a): "))

if Peso <= 20:
  print(f'O(A) lutador(a) {Nome} precisa ganhar uns quilinhos')
elif Peso < 65:
  print(f'O(A) lutador(a) {Nome} pesa {Peso} kg e se enquadra na categoria Pena')
elif Peso < 72:
  print(f'O(A) lutador(a) {Nome} pesa {Peso} kg e se enquadra na categoria Leve')
elif Peso < 79:
  print(f'O(A) lutador(a) {Nome} pesa {Peso} kg e se enquadra na categoria Ligeiro')
elif Peso < 86:
  print(f'O(A) lutador(a) {Nome} pesa {Peso} kg e se enquadra na categoria Meio médio')
elif Peso < 93:
  print(f'O(A) lutador(a) {Nome} pesa {Peso} kg e se enquadra na categoria Médio')
elif Peso < 100:
  print(f'O(A) lutador(a) {Nome} pesa {Peso} kg e se enquadra na categoria Meio pesado')
else:
  print(f'O(A) lutador(a) {Nome} pesa {Peso} kg e se enquadra na categoria Pesado')