menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
quantidade_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            print("Valor depositado")
            print(f"Seu novo saldo é R$ {saldo:.2f}")
            extrato.append(f"Deposito feito de R$ {valor:.2f}")

        else:
            print("Valor invalido!")
    
    elif opcao == "s":
        valor_saque = float(input("Informe o valor do saque: "))

        if quantidade_saques < LIMITE_SAQUES and valor_saque < saldo and valor_saque < limite: #limite disponivel
            saldo -= valor_saque
            print("Saque realizado")
            print(f"Saldo remanescente R$ {saldo:.2f}")
            quantidade_saques += 1
            extrato.append(f"Saque realizado no valor de R$ {valor_saque:.2f}")

        elif quantidade_saques < LIMITE_SAQUES and valor_saque > saldo: #saldo insuficiente
            print("Voce nao tem saldo suficiente.")
        
        elif quantidade_saques >= LIMITE_SAQUES: #limite de saques excedido
            print("Voce ultrapassou o limite de saques diarios.")

        elif quantidade_saques < LIMITE_SAQUES and valor_saque > limite: #valor do saque acima do limite
            print(f"Voce ultrapassou o limite do valor do saque de R${limite:.2f}, tente um valor menor.")
        
        else:
            print("Valor invalido!")


    elif opcao == "e":
        for indice, lista in enumerate(extrato):
            print(f"{indice}: {lista}")
        print(f"Seu saldo atual é de {saldo:.2f}")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

