Peca1String = input().split(sep=' ')
CodPeca1 = int(Peca1String[0])
QtdPeca1 = int(Peca1String[1])
ValorPeca1 = float(Peca1String[2])

Peca2String = input().split(sep=' ')
CodPeca2 = int(Peca2String[0])
QtdPeca2 = int(Peca2String[1])
ValorPeca2 = float(Peca2String[2])

ValorTotal = (QtdPeca1 * ValorPeca1) + (QtdPeca2 * ValorPeca2)
print(f'VALOR A PAGAR: R$ {ValorTotal:.2f}')