import re
import random


'''
usuarios = {
    "numero_conta" : {
        "cpf" : "",
        "nome" : "",
        "data_nascimento" : "",
        "endereco" : "",
        "saldo" : 0.0,
        "extrato" : {
            "saques": [],
            "depositos": []
        }
    }
}
'''

usuarios = {}
contas_registradas = set()
numero_saques_dia = 0
valor_max_saque = 500
LIMITE_SAQUES = 3

def limpar_cpf(cpf: str) -> str:
    '''
    args: cpf: str - CPF do usuário
    returns: str - CPF limpo, contendo apenas números
    Descrição: Remove caracteres não numéricos do CPF e valida seu comprimento. Não trata CPF inválido com fórmula geradora.
    '''

    cpf_limpo = re.sub(r'[^0-9]', '', cpf)
        
    if len(cpf_limpo) != 11:
        raise ValueError ("CPF inválido! O cpf deve conter 11 caracteres NUMÉRICOS.") 
        
    return cpf_limpo
    
def sacar (valor: float, numero_conta):
    '''
    args: valor: float - valor do saque
           numero_conta: int - número da conta do usuário
    returns: None
    Descrição: Realiza o saque do valor especificado da conta do usuário.
    '''
    global numero_saques_dia, valor_max_saque, usuarios
    valor = float(valor)
     
    if numero_conta not in usuarios:
        raise ValueError("Conta não encontrada. Verifique o número da conta.")

    saldo = usuarios[numero_conta]["saldo"]
    
    if valor > valor_max_saque:
        raise ValueError(f"\nValor máximo de saque é R$ {valor_max_saque: .2f}.")
        
    elif valor < saldo and numero_saques_dia < LIMITE_SAQUES:
        saldo -= valor
        numero_saques_dia += 1

        usuarios[numero_conta]["saldo"] = saldo
        usuarios[numero_conta]["extrato"]["saques"].append(valor)
        print(f"\nSaque de R${valor:.2f} concluído.\nSaldo atual: R${saldo:.2f}.")
        
    else:
        print(f"\n[ERRO] - Saldo insuficiente ou limite de saques atingido. Seu saldo: {saldo}, Saques hoje: {numero_saques_dia}.")
        
    
def depositar (valor: float, numero_conta):
    '''
    args: 
        valor: float - valor do depósito
        numero_conta: int - número da conta do usuário
    
    returns: None
    Descrição: Realiza o depósito do valor especificado na conta do usuário.
    '''
    global usuarios
    
    if not re.match(r'[0-9.,]+', str(valor)):
        raise ValueError("Valor inválido. Use apenas números e vírgulas ou pontos para separar decimais.")
    
    
    if numero_conta not in usuarios:
        raise ValueError("Conta não encontrada. Verifique o número da conta.")
    
    saldo = usuarios[numero_conta]["saldo"]

    
    if valor > 0:
        saldo += valor

        usuarios[numero_conta]["saldo"] = saldo
        usuarios[numero_conta]["extrato"]["depositos"].append(valor)
        print(f"\nDepósito de R${valor:.2f} concluído.\nSaldo atual: R${saldo:.2f}.")
        
    else:
        print("\n[ERRO] - Valor inválido para depósito. Use um valor maior que 0.")
    
def extrato(numero_conta):
    '''
    args: numero_conta: int - número da conta do usuário
    returns: None
    Descrição: Exibe o extrato da conta do usuário, incluindo saques, depósitos e saldo atual.
    '''
    global usuarios
    
    if numero_conta not in usuarios:
        raise ValueError("Conta não encontrada. Verifique o número da conta.")
    
    saques = usuarios[numero_conta]["extrato"]["saques"]
    depositos = usuarios[numero_conta]["extrato"]["depositos"]
    saldo = usuarios[numero_conta]["saldo"]
    
    print("\n========== Extrato ==========\n")
    
    if len(saques)!=0:
        print("Saques realizados:")
        for saque in saques:
            print (f"- R${saque:.2f}\n")
    
    if len(depositos)!=0:    
        print("Depósitos realizados:")
        for deposito in depositos:
            print (f"+ R${deposito:.2f}\n")
        
    print(f"Saldo atual: R${saldo:.2f}")
    
    print("=============================")
    
def cadastrar_usuario():
    '''
    args: None
    returns: None
    Descrição: Coleta informações do usuário para criar uma nova conta bancária. '''
    global usuarios, contas_registradas

    cpf = input("Digite seu CPF: ")
    cpf = limpar_cpf(cpf)

    if any(usuario["cpf"] == cpf for usuario in usuarios.values()):
        raise ValueError("Já existe uma conta associada à esse CPF..")

    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    endereco = input("Digite seu endereço: ")
    
    while True:
        numero_conta = random.randint(1000, 9999)
        if numero_conta not in contas_registradas:
            break
        
    numero_conta = str(numero_conta)       
    
    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco,
        "numero_conta": numero_conta,
        "saldo": 0.0,
        "extrato": {
            "saques": [],
            "depositos": []	
        }
    }
    
    contas_registradas.add(numero_conta)
    usuarios[numero_conta] = usuario

    print(f"{nome}, sua conta foi criada com sucesso. Seu número da conta é {numero_conta}.")
    return numero_conta

def listar_contas():
    '''
    args: None
    returns: None
    Descrição: Lista todas as contas registradas no sistema, exibindo numero de conta e CPF relacionado.
    '''
    global usuarios
    
    if not usuarios:
        print("Nenhuma conta registrada.")
        return
    
    print("\n========== Contas Registradas ==========\n")
    
    for numero_conta, usuario in usuarios.items():
        print(f"Conta: {numero_conta} / CPF: {usuario['cpf']}")
    
    print("=========================================")