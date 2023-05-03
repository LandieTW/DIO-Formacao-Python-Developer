"""
Fomos contratados por um grande banco para desenvolver o seu novo sistema. 
Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. 
Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

1 - OPERAÇÃO DE DEPÓSITO
Deve ser possível depositar valores positivos para a minha conta bancária. 
A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. 
Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

2 - OPERAÇÃO DE SAQUE
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. 
Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. 
Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

3 - OPERAÇÃO DE EXTRATO
Essa operação deve listar todos os depósitos e saques realizados na conta. 
No fim da listagem deve ser exibido o saldo atual da conta. 
Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
"""

conta = 0

while True:

    acao = input("O que desejas fazer? \n d = Depositar \n s = Sacar \n e = Extrato \n")

    if acao == "d":
        deposito = float(input("Qual valor desejas depositar? "))
        
        if deposito < 0:
            print("Não é possível depositar um valor negativo.")
        else:
            conta += deposito
            print(f"Você depositou R$ {deposito:.2f}")

    elif acao == "s":
        saque = float(input("Qual valor desejas sacar? "))

        if saque > conta:
            print("Você não possui o saldo disponível para efetuar este saque.")
        else:
            conta -= saque
            print(f"Você sacou R$ {saque:.2f}")

    elif acao == "e":
        print(f"Seu saldo é de: R$ {conta:.2f}")

    else:
        break
