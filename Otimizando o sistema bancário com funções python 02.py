"""
Separar as funções existentes de saque, depósito e extrato em funções.
Criar duas novas funções: cadastrar usuários (clientes) e cadastrar conta bancária

DESAFIO
Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar,
depositar e visualizar histórico.
Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: criar usuário (cliente do banco) e
criar conta corrente (vincular com usuário)

SEPARAÇÃO EM FUNÇÕES
Devemos criar funções para todas as operações do sistema.
Para exercitar tudo o que aprendemos neste módulo, cada função vai ter uma regra na passagem de argumentos.
O retorno e a forma como serão chamadas, pode ser definida por você da forma que achar melhor.
"""


usuarios = []
contas = []
historico = []


def cadastrar_usuario(nome: str, data_de_nascimento: str, cpf: str, endereco:str) -> list:

    """O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e
    endereço.
    O endereço é uma string com o formato: logradouro, numero, bairro, cidade/sigla estado.
    Deve ser armazenado somente os números do CPF.
    Não podemos cadastrar 2 usuários com o mesmo CPF."""

    novo_usuario = [nome, data_de_nascimento, cpf, endereco]

    if len(usuarios) > 0:
        for i in range(len(usuarios)):
            if usuarios[i][2] != cpf:
                usuarios.append(novo_usuario)
                print("\n Usuário cadastrado com sucesso! \n")
            else:
                print('Já existe um usuário cadastrado neste CPF.')
    else:
        usuarios.append(novo_usuario)
        print("\n Usuário cadastrado com sucesso! \n")


def cadastrar_conta_bancaria(usuario: str, saldo: float = 0.0, limite: float = 10_000.0, limite_saques: int = 10,
                             conta: int = (len(contas) + 1), agencia: str ="0001") -> list:

    """O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário.
    O número da conta é sequencial, iniciando em 1.1

    O número da agência é fixo: "0001".
    O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário."""

    for k in range(len(usuarios)):
        if usuarios[k][0] == usuario:
            nova_conta = [agencia, conta, usuario, float(saldo), limite, limite_saques]
            contas.append(nova_conta)
            print("\n Conta aberta com sucesso! \n")
        else:
            print("Usuário não cadastrado.")


def listar_contas():
    
    """Apresenta todas as contas já cadastradas"""

    for conta in contas:
        print(conta)


def sacar(nome: str, valor: float):

    """Função que rege os saques nas contas do usuário"""

    contador_saque = 0

    for n in range(len(contas)):
        if contas[n][2] == nome:
            if float(valor) < contas[n][3]:
                if contas[n][5] > 0:

                    contador_saque += 1
                    contas[n][5] -= contador_saque

                    saldo = contas[n][3]
                    q = saldo - float(valor)
                    extrato = (nome , saldo, valor, q)
                    historico.append(extrato)

                    print(f'Seu saque foi realizado com sucesso, {nome}. Segue abaixo o seu extrato.')
                    print(extrato[1])
                    print(extrato[2])
                    print(extrato[3])
                
                else:
                    print(f'Desculpe, {nome}, você já atingiu o seu limite de saques.')
            else:
                print(f'Desculpe, {nome}, você não possui saldo suficiente para realizar este saque.')
        else:
            print('Usuário não encontrado.')


def depositar(nome: str, valor: float):

    """Função que rege os depósitos nas contas do usuário"""

    for n in range(len(contas)):
        if contas[n][2] == nome:

            saldo = contas[n][3]
            p = saldo + float(valor)
            contas[n][3] += p

            extrato = (nome , f'Saldo inicial: R$ {saldo:.2f}',f'Depósito: R$ {float(valor):.2f}',f'Saldo final: R$ {p:.2f}')
            historico.append(extrato)

            print(f'Seu depósito foi realizado com sucesso, {nome}. Segue abaixo o seu extrato.')
            print(extrato[1])
            print(extrato[2])
            print(extrato[3])
                
        else:
            print('Usuário não encontrado.')


def visualizar_historico(nome: str):

    """Função que possibilita visualizar o histórico de operações na conta de um determinado usuário"""

    for z in range(len(historico)):
        if historico[z][0] == nome:
            print(historico[z][1])
            print(historico[z][2])
            print(historico[z][3])


conta = 0
















while True:

    acao = input("""\n O que desejas fazer? \n 
                    1 = Cadastrar usuário \n 
                    2 = Cadastrar conta \n 
                    3 = Lista contas \n 
                    4 = Saques \n
                    5 = Depósitos \n
                    6 = Visualizar histórico \n
                    7 = Sair \n""")

    if acao == "1":

        informacao_nome = input("Qual o seu nome? ")
        informacao_nascimento = input("Qual a sua data de nascimento? ")
        informacao_cpf = input("Informe o seu CPF (somente números) ")
        informacao_endereco = input("Informe o seu endereço. ")

        cadastrar_usuario(informacao_nome, informacao_nascimento, informacao_cpf, informacao_endereco)

    elif acao == "2":
        
        informacao_nome = input("Qual o seu nome? ")

        cadastrar_conta_bancaria(informacao_nome)

    elif acao == "3":

        print("agencia, conta, usuario, saldo, limite, limite_saques")
        listar_contas()

    elif acao == "4":
        
        informacao_nome = input("Qual o seu nome?")
        informacao_valor = input("Qual valor você deseja sacar?")

        sacar(informacao_nome, informacao_valor)

    elif acao == "5":
        
        informacao_nome = input("Qual o seu nome?")
        informacao_valor = input("Qual valor você deseja depositar?")

        depositar(informacao_nome, informacao_valor)

    elif acao == "6":
        
        informacao_nome = input("Qual o seu nome?")

        visualizar_historico(informacao_nome)

    elif acao == "7":
        break

    else:
        print("\n Você digitou uma opção incorreta. \n")
