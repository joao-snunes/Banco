from funcoes import *
    
menu = """
========== Banco ==========
1 - Sacar
2 - Depositar
3 - Extrato
4 - Sair
===========================
==>"""
    
while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        valor =input("Digite o valor do saque: R$")
        sacar(float(valor))
        
    elif opcao == "2":
        valor = input("Digite o valor do depósito: R$")
        depositar(float(valor))
    
    elif opcao == "3":
        extrato()
        
    elif opcao == "4":
        print("saindo...")
        break
        
    else:
        print("Opção inválida! Tente novamente.")