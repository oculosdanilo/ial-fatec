# pdf: https://www.clictec.com.br/ial002m/aulas/IAL002_PrjN2C_2024.2_EstoqueOperacional.pdf
# Projeto Estoque - 22/11
#   Antonio Marcos Freitas da Silva
#   Danilo Carvalho Lima
#   Marina Gusmão Faria Barbosa Bueno
#   Vinicius Coutinho de Castro

def ExisteCodigo(Codigo, Lista):
  for item in Lista:
    if item["codigo"] == Codigo:
      return True

  return False


def IndexLista(Codigo, Lista):
  cont = 0
  for item in Lista:
    if item["codigo"] == Codigo:
      return cont
    cont += 1


def sortLista(e):
  return int(e["codigo"])


# {
#   "codigo": string,
#   "qtdEstoque": int,
#   "qtdMinima": int
# }
ProdutosLista = []

ArquivoProdutos = open("PRODUTOS.TXT", "r")
for Produto in ArquivoProdutos:
  Produto = Produto.strip().split(";")
  ProdutosLista.append({
    "codigo": Produto[0],
    "qtdEstoque": int(Produto[1]),
    "qtdMinima": int(Produto[2]),
  })
ArquivoProdutos.close()

# {
#   "divergencia": int, (1 = nao tem codigo, 2 = venda cancelada, 3 = venda nao finalizada, 4 = erro desconhecido)
#   "linha": int,
#   "codigo": string (se necessário)
# }
DivergenciasLista = []

# {
#   "codigo": string,
#   "qtdVendida": int
# }
VendasLista = []

CanalVendasLista = {
  1: 0,  # representantes
  2: 0,  # website
  3: 0,  # android
  4: 0,  # iphone
}

ArquivoVendas = open("VENDAS.TXT", "r")
ContadorVendas = 1
for Venda in ArquivoVendas:
  Venda = Venda.strip().split(";")
  if Venda[2] == "135":
    DivergenciasLista.append({
      "divergencia": 2,
      "linha": ContadorVendas,
    })
  elif Venda[2] == "190":
    DivergenciasLista.append({
      "divergencia": 3,
      "linha": ContadorVendas,
    })
  elif Venda[2] == "999":
    DivergenciasLista.append({
      "divergencia": 4,
      "linha": ContadorVendas,
    })
  else:  # vendas com situação 100 ou 102
    if ExisteCodigo(Venda[0], ProdutosLista):
      CanalVendasLista[int(Venda[3])] += int(Venda[1])  # adiciona as vendas a seu respectivo canal
      if ExisteCodigo(Venda[0], VendasLista):
        # se ja existir o codigo na lista, só acrescentar no valor existente
        indexVenda = IndexLista(Venda[0], VendasLista)
        VendasLista[indexVenda]["qtdVendida"] += int(Venda[1])
      else:
        # senão criar uma nova venda
        VendasLista.append({
          "codigo": Venda[0],
          "qtdVendida": int(Venda[1]),
        })
    else:
      DivergenciasLista.append({
        "divergencia": 1,
        "linha": ContadorVendas,
        "codigo": Venda[0],
      })

  ContadorVendas += 1
ArquivoVendas.close()

Divergencias = ""
ArquivoDivergencias = open("DIVERGENCIAS.TXT", "w", encoding='utf-8')
for Divergencia in DivergenciasLista:
  linha = Divergencia["linha"]
  match Divergencia["divergencia"]:
    case 1:
      Divergencias += f"Linha {linha:3} - Código de Produto não encontrado {Divergencia["codigo"]:5}\n"
    case 2:
      Divergencias += f"Linha {linha:3} - Venda cancelada\n"
    case 3:
      Divergencias += f"Linha {linha:3} - Venda não finalizada\n"
    case _:
      Divergencias += f"Linha {linha:3} - Erro desconhecido. Acionar equipe de TI.\n"

ArquivoDivergencias.write(Divergencias)
ArquivoDivergencias.close()

ArquivoCanalVendas = open("TOTCANAL.TXT", "w", encoding='utf-8')
CanalVendas = ("Quantidades de Vendas por canal\n\n"
               "Canal                  QtVendas\n"
               f"1 - Representantes     {CanalVendasLista[1]:8}\n"
               f"2 - Website            {CanalVendasLista[2]:8}\n"
               f"3 - App móvel Android  {CanalVendasLista[3]:8}\n"
               f"4 - App móvel iPhone   {CanalVendasLista[4]:8}\n")
ArquivoCanalVendas.write(CanalVendas)
ArquivoCanalVendas.close()

VendasLista.sort(key=sortLista)

Transfere = ("Necessidade de Transferência Armazém para CO\n\n"
             "Produto  QtCO  QtMin  QtVendas  Estq.após  Necess. Transf. de\n"
             "                                   Vendas           Arm p/ CO\n")
for Venda in VendasLista:
  Produto = ProdutosLista[IndexLista(Venda["codigo"], ProdutosLista)]
  estqAposVendas = Produto['qtdEstoque'] - Venda['qtdVendida']
  necess = 0
  if estqAposVendas < Produto['qtdMinima']:
    necess = Produto['qtdMinima'] - estqAposVendas
  transf = 0
  if 0 < necess <= 10:
    transf = 10
  else:
    transf = necess
  Transfere += f"{Venda['codigo']}    {Produto['qtdEstoque']:4}  {Produto['qtdMinima']:5}  {Venda['qtdVendida']:8}  {estqAposVendas:9}  {necess:7}  {transf:9}\n"

ArquivoTransfere = open("TRANSFERE.TXT", "w", encoding='utf-8')
ArquivoTransfere.write(Transfere)
ArquivoTransfere.close()
