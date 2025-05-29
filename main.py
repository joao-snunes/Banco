from funcoes import *
    
menu = """
========== Banco ==========
1- Criar conta
2 - Sacar
3 - Depositar
4 - Extrato
5 - Listar Contas
6 - Sair
===========================
==>"""
    

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        print("para criar sua conta, vamos precisar de alguns dados...")
        try:
            cadastrar_usuario()
        except ValueError as e:
            print(e)
            continue
        
    elif opcao == "2":
        valor =input("Digite o valor do saque: R$")
        conta = input("Digite o número da conta: ")
        try:
            sacar(float(valor), conta)
        except ValueError as e:
            print(e)
            continue
        
    elif opcao == "3":
        valor = input("Digite o valor do depósito: R$")
        conta = input("Digite o número da conta: ")
        try:
            depositar(float(valor), conta)
        except ValueError as e:
            print(e)
            continue
    
    elif opcao == "4":
        conta = input("Digite o número da conta: ")
        try:
            extrato(conta)
        except ValueError as e:
            print(e)
            continue
        
    elif opcao == "5":
        listar_contas()
        
    elif opcao == "6":
        print("saindo...")
        break
        
    else:
        print("Opção inválida! Tente novamente.")
'''    
try:
    conta = cadastrar_usuario()

    if conta in usuarios and isinstance(conta, str):
        print("Conta criada com sucesso!")
        #depositar(100, conta)
        print("saldo", usuarios[conta]["saldo"])
        extrato(conta)
except ValueError as e:
    print(e)
'''