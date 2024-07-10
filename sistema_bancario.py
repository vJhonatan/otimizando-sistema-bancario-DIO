import os
import time

# Deposito
def depositar(saldo, extrato):
    deposito = float(input("Deposite o valor que deseja: "))

    if (deposito > 0):
        saldo += deposito
        extrato += (f"Deposito: R$ {deposito:.2f}\n")
        print("Deposito efetuado com sucesso!")
        time.sleep(2.5)
        os.system('cls')
    else:
        print("Erro ao depositar! Tente novamente.")
        time.sleep(2.5)
        os.system('cls')

    return saldo, extrato

# Saque
def sacar(saldo, extrato, qtd_saques, limite, LIMITE_SAQUES):
    saque = float(input("Informe a quantia que deseja sacar: "))

    saldo_insuficiente = saque > saldo
    limite_atingido = saque > limite
    limite_saques_diario = qtd_saques >= LIMITE_SAQUES

    if saldo_insuficiente:
        print("Erro ao efetuar saque! Saldo insuficiente.")
        time.sleep(2.5)
        os.system('cls')

    elif limite_atingido:
        print("Erro ao efetuar saque! Saque deve ser no máximo de R$ 500,00.")
        time.sleep(2.5)
        os.system('cls')

    elif limite_saques_diario:
        print("Erro ao efetuar saque! Limite de saques diário atingido.")
        time.sleep(2.5)
        os.system('cls')

    elif saque > 0:
        saldo -= saque
        extrato += (f"Saque: R$ {saque:.2f}\n")
        qtd_saques += 1
        print("Saque efetuado com sucesso!")
        time.sleep(2.5)
        os.system('cls')

    else:
        print("Erro ao efetuar saque! O valor informado é inválido.")
        time.sleep(2.5)
        os.system('cls')

    return saldo, extrato, qtd_saques

# Extrato
def extratos(saldo, extrato):
    os.system('cls')
    print("  EXTRATO BANCARIO")
    print("=====================\n")
    print(extrato)
    print(f"\nSaldo Atual: R$ {saldo:.2f}")
    print("=====================\n")

# Cadastro de usuário
def novo_usuario(usuarios):
    cpf = input("Informe o seu CPF (Apenas Números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Este CPF já está em uso! Tente novamente.")
        time.sleep(2)
        os.system('cls')
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf})
    
    print("Usuário Criado com Sucesso!")
    time.sleep(2)
    os.system('cls')

# Filtrar CPF do Usuário
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

# Criar Conta Bancária
def nova_conta_bancaria(usuarios, NUM_AGENCIA, num_conta):
    cpf = input("Informe o seu CPF (Apenas Números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Conta Bancária criada com sucesso!")
        time.sleep(2)
        os.system('cls')
        return {"NUM_AGENCIA": NUM_AGENCIA, "num_conta": num_conta, "usuario": usuario}
    
    print("Usuário não encontrado, confira se já tem cadastro em seu CPF.")
    time.sleep(2)
    os.system('cls')
    return

# Listar Contas
def listar_contas(contas_bancarias):
    
    if contas_bancarias:
        for conta in contas_bancarias:
            texto = f"""
                Agência: {conta['NUM_AGENCIA']}
                Número da Conta: {conta['num_conta']}
                Titular: {conta['usuario']['nome']} \n
            """
            print(texto)
        time.sleep(3)
        os.system('cls')
        return
    else:
        print("Nenhuma conta registrada até o momento.")
        time.sleep(2)
        os.system('cls')
        return
        
    

menu = """
    ----SISTEMA BANCÁRIO----
    
         (1) Depósito
         (2) Saque
         (3) Extrato
         
         (4) Novo Usuário
         (5) Nova Conta Bancária
         (6) Listar Contas
            
         (0) Sair
"""

NUM_AGENCIA = '0001'
LIMITE_SAQUES = 3

saldo = 0
limite = 500
extrato = ""
qtd_saques = 0
usuarios = []
contas_bancarias = []
num_conta = 1

while True:
    opcao = int(input(menu))

    # Depósito
    if opcao == 1:
        saldo, extrato = depositar(saldo, extrato)

    # Saque
    elif opcao == 2:
        saldo, extrato, qtd_saques = sacar(saldo, extrato, qtd_saques, limite, LIMITE_SAQUES)

    # Extrato
    elif opcao == 3:
        extratos(saldo, extrato)

    # Novo Usuário
    elif opcao == 4:
        novo_usuario(usuarios)

    # Nova Conta
    elif opcao == 5:
        conta = nova_conta_bancaria(usuarios, NUM_AGENCIA, num_conta)
        
        if conta:
            num_conta += 1
            contas_bancarias.append(conta)

    # Listar Contas
    elif opcao == 6:
        listar_contas(contas_bancarias)    

    elif opcao == 0:
        os.system('cls')
        break

    else:
        print("\nOpção Inválida! Selecione uma das opções.")
        time.sleep(2.5)
        os.system('cls')
