saques = []
depositos = []
saldo = 0.0
numero_saques_dia = 0
valor_max_saque = 500
LIMITE_SAQUES = 3

def sacar (valor):
    global saldo, numero_saques_dia
    
    if valor > 500:
        print("Valor máximo de saque é R$ 500,00.")
        return
    
    elif valor < saldo and numero_saques_dia < LIMITE_SAQUES:
        saldo -= valor
        numero_saques_dia += 1
    
        saques.append(valor)
        
    else:
        print(f"Saldo insuficiente ou limite de saques atingido. Seu saldo: {saldo}, Saques hoje: {numero_saques_dia}.")
        
    
def depositar (valor):
    global saldo
    
    if valor > 0:
        saldo += valor
        
        depositos.append(valor)
        
    else:
        print("Valor inválido para depósito. Use um valor maior que 0.")
    
def extrato():
    global saldo
    
    print("\n========== Extrato ==========\n")
    
    if len(saques)!=0:
        print("Saques realizados:")
        for saque in saques:
            print (f"- R${saque:.2f}\n")
    
    if len(depositos)!=0:    
        print("Depósitos realizados:")
        for deposito in depositos:
            print (f"- R${deposito:.2f}\n")
        
    print(f"Saldo atual: R${saldo:.2f}")
    
    print("=============================")