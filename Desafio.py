import Funções_Desafio

LIMITE_DE_SAQUES = 3
AGENCIA = '0001'

saldo = 0
limite_por_saque = 500
extrato_conta = []
numero_de_saques = 0
usuarios = []
contas = []

while True:
    try:
        Funções_Desafio.menu()
        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:

            saldo, extrato_conta = Funções_Desafio.deposito(saldo, extrato_conta)
            Funções_Desafio.carregando('Fazendo deposito!', 'Valor depositado com sucesso!')

        elif opcao == 2:
            saldo, extrato_conta, LIMITE_DE_SAQUES = Funções_Desafio.saque(saldo=saldo, extrato_conta=extrato_conta, limite_de_saques=LIMITE_DE_SAQUES, limite_por_saque=limite_por_saque)

        elif opcao == 3:
            Funções_Desafio.extrato(extrato_conta, saldo=saldo)

        elif opcao == 4:
            cliente = Funções_Desafio.criar_usuario()

            if not any(usuario.get('cpf') == cliente.get('cpf') for usuario in usuarios):
                usuarios.append(cliente)
                print('Usuário criado com sucesso!')
            else:
                print('Usuário já existe!')

        elif opcao == 5:
            Funções_Desafio.carregando('Saindo do sistema!', 'Obrigado por ultilizar nosso sistema, até a proxima :)')
            break

        else:
            print('Opção invalida, escolha uma das opções acima! ')
            continue

        verificacao = Funções_Desafio.verificacao_s_ou_n()

        if verificacao == 'N':
            Funções_Desafio.carregando('Saindo do sistema!', 'Obrigado por ultilizar nosso sistema, até a proxima :)')
            break

    except ValueError:
        print('Valor invalido, tente uma das opcoes abaixo!')
