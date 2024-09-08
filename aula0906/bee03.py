ddd = int(input())

cidade = ""
match ddd:
  case 61:
    cidade = "Brasilia"
  case 71:
    cidade = "Salvador"
  case 11:
    cidade = "Sao Paulo"
  case 21:
    cidade = "Rio de Janeiro"
  case 32:
    cidade = "Juiz de Fora"
  case 19:
    cidade = "Campinas"
  case 27:
    cidade = "Vitoria"
  case 31:
    cidade = "Belo Horizonte"
  case _:
    cidade = "DDD nao cadastrado"

print(cidade)