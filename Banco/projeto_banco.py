def main(): 
    saldo = 0
    limite = 500
    extrato = []
    quantidade_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
    quantidade_contas = 0
    
    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s": 
            valor_saque = float(input("Informe o valor do saque: "))
            saldo, extrato, quantidade_saques = sacar(saldo=saldo, 
                                                    valor_saque=valor_saque, 
                                                    extrato=extrato, 
                                                    limite=limite, 
                                                    quantidade_saques=quantidade_saques, 
                                                    LIMITE_SAQUES=LIMITE_SAQUES,
                                                    )
            
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "u":
            cadastrar_usuario(usuarios)

        elif opcao == "nc":
            quantidade_contas = criar_conta(usuarios, quantidade_contas, AGENCIA, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            
def sacar(*, saldo, valor_saque, extrato, limite, quantidade_saques, LIMITE_SAQUES):   
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
    
    return saldo, extrato, quantidade_saques

def depositar(saldo, valor, extrato, /):
    if valor > 0:
                saldo += valor
                print("Valor depositado")
                print(f"Seu novo saldo é R$ {saldo:.2f}")
                extrato.append(f"Deposito feito de R$ {valor:.2f}")

    else:
        print("Valor invalido!")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    for indice, lista in enumerate(extrato):
        print(f"{indice}: {lista}")
    print(f"Seu saldo atual é de {saldo:.2f}")

def cadastrar_usuario(usuarios):
    cpf = input("Gentileza, informe seu CPF (Somente os numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Usuario com esse CPF já existente!")
        return
    
    nome = input("Gentileza, insira seu nome completo: ")
    data_nascimento = input("Agora informe sua data de nascimento: ")
    endereco = input("Por ultimo, informe seu endereço(logradouro, nro, bairro, Municipio-UF): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": [endereco]})
    print("Usuario cadastrado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(usuarios, quantidade_contas, AGENCIA, contas):
    cpf = input("Digite seu cpf(apenas numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        quantidade_contas += 1
        contas.append({"agencia": AGENCIA, "numero_conta": quantidade_contas, "usuario": usuario})
        print(f"Sua conta foi criada! Agencia: {AGENCIA} e numero da conta: {quantidade_contas}")
    else:
        print("Usuario nao existente!")
    
    return quantidade_contas

    
def listar_contas(contas):
    for conta in contas:
        print(conta)
    

def menu():
    menu = """
    $$ Bem-vindo ao menu do banco $$
    - selecione sua opçao
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Cria usuario
    [nc] Nova conta
    [lc] Listar contas
    [q] Sair

    => """

    return input(menu)

main()