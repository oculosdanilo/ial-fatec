mes = int(input())

mesExtenso = ""
match mes:
  case 1:
    mesExtenso = "January"
  case 2:
    mesExtenso = "February"
  case 3:
    mesExtenso = "March"
  case 4:
    mesExtenso = "April"
  case 5:
    mesExtenso = "May"
  case 6:
    mesExtenso = "June"
  case 7:
    mesExtenso = "July"
  case 8:
    mesExtenso = "August"
  case 9:
    mesExtenso = "September"
  case 10:
    mesExtenso = "October"
  case 11:
    mesExtenso = "November"
  case 12:
    mesExtenso = "December"

print(mesExtenso)
