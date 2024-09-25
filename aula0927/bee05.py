vert = input()
classe = input()
dieta = input()

match vert:
  case "vertebrado":

    match classe:
      case "ave":

        match dieta:
          case "carnivoro":
            print("aguia")
          case _:
            print("pomba")

      case _:
        match dieta:
          case "onivoro":
            print("homem")
          case _:
            print("vaca")

  case _:
    match classe:
      case "inseto":

        match dieta:
          case "hematofago":
            print("pulga")
          case _:
            print("lagarta")

      case _:
        match dieta:
          case "hematofago":
            print("sanguessuga")
          case _:
            print("minhoca")
