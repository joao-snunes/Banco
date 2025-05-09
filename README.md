# Projeto de Sistema Bancario

## Objetivo
Introduzir conceitos básicos, treinar sintaxe e funcionalidades da linguagem. Este projeto foi elaborado como parte do Bootcamp DIO/Vivo para aplicações de AI utilizando python e será aprimorado com o passar do tempo.

## Composição do projeto
Composto por, até então, dois arquivos .py, um deles (funcoes.py) contendo a definição das funções utilizadas no sistema (Sacar, Depositar e Extrato), e main.py onde as mesmas são utilizadas em um menu interativo.

## Descrição das funções

### 1- Sacar
Permite que o usuário faça saques de até R$ 500,00 dentro do sistema, o usuário é restrito à 3 saques por execução desde que o valor esteja de acordo com o saldo. Recebe o valor da transação como parâmetro.

### 2- Depositar
Permite que o usuário faça depósitos no sistema, a única restrição aqui é que o valor a ser depositado seja positivo. Recebe o valor da transação como parâmetro.

### 3- Extrato
Exibe todas as transações de saque e depósito realizadas pelo usuário, além de exibir o saldo em conta. Essa função não recebe parâmetros.

### 4- Sair
O loop de menu é "quebrado" e o programa é finalizado.
