def criar_usuario():
    try:
        nome = input('Digite seu nome: ')

        # Loop para garantir que a data de nascimento esteja no formato correto
        while True:
            data_nascimento = input('Digite sua data de nascimento (DD/MM/AAAA): ')
            try:
                dia, mes, ano = data_nascimento.split('/')
                if len(dia) == 2 and len(mes) == 2 and len(ano) == 4:
                    dia, mes, ano = int(dia), int(mes), int(ano)
                    break
                else:
                    print('Data de nascimento no formato inválido. Por favor, digite novamente.')
            except ValueError:
                print('Data de nascimento no formato inválido. Por favor, digite novamente.')

        # Loop para garantir que o CPF seja numérico e tenha 11 dígitos
        while True:
            cpf = input('Digite seu CPF (Somente números): ')
            if cpf.isdigit() and len(cpf) == 11:
                break
            else:
                print('CPF inválido. Deve conter 11 dígitos numéricos. Por favor, digite novamente.')

        print('Digite seu endereço!')
        logradouro = input('Logradouro: ')
        numero = input('Número da residência: ')
        bairro = input('Bairro: ')
        cidade = input('Cidade / Sigla do Estado: ')
        endereco = f'{logradouro}, {numero}, {bairro}, {cidade}'

        cliente = {
            'nome': nome,
            'data_nascimento': data_nascimento,
            'cpf': cpf,
            'endereco': endereco
        }

        return cliente

    except Exception as e:
        print(f'Ocorreu um erro inesperado: {e}')


def deposito(saldo, extrato_conta, /):
    while True:
        valor_a_depositar = int(input('Quanto você deseja depositar?: '))
        try:

            if valor_a_depositar <= 0:
                print('Não é possivel depositar esse tipo de valor!\nTente um valor inteiro acima de 0!')

            else:
                saldo += valor_a_depositar
                extrato_conta.append('Deposito')
                extrato_conta.append(f'    + R${valor_a_depositar}')
                return saldo, extrato_conta

        except ValueError:
            print('Valor digitado incorreto!, Aceitamos apenas valores inteiros!')


def saque(*, saldo, extrato_conta, limite_de_saques, limite_por_saque):
    while True:
        try:
            valor_a_sacar = int(input('Quanto você deseja sacar?: '))

            if saldo == 0:
                print('Não foi possivel realizar o saque!\nVocê não tem valores disponiveis para sacar!')
                print(f'Seu saldo atual é de R${saldo:.2f}')
                return saldo, extrato_conta, limite_de_saques

            elif valor_a_sacar > saldo:
                carregando('Fazendo saque!',
                           'Não foi possivel realizar o saque!\nO valor que deseja sacar e menor do que seu saldo!'
                           )
                print(f'Seu saldo atual é de R${saldo:.2f}')

            elif valor_a_sacar > limite_por_saque:
                print(f'Não foi possivel realizar o saque!\nO valor limite por saque é de R${limite_por_saque:.2f}!')

            elif limite_de_saques == 0:
                carregando('Fazendo saque!', f'Não foi possivel realizar o saque!\nO limite de saque diario excedeu!')
                print('Tente novamente amanhã!')
                return saldo, extrato_conta, limite_de_saques

            else:
                saldo -= valor_a_sacar
                limite_de_saques -= 1
                extrato_conta.append('Saque')
                extrato_conta.append(f'    - R${valor_a_sacar}')
                carregando('Fazendo saque!', 'Saque realizado com sucesso!')
                return saldo, extrato_conta, limite_de_saques

        except ValueError:
            print('Valor digitado incorreto!, Aceitamos apenas valores inteiros!')


def extrato(extrato_conta, /, *, saldo):
    carregando('Exibindo extrato', '')
    print('=-=-=-=-=-= EXTRATO =-=-=-=-=-')
    for i in range(0, len(extrato_conta)):
        print(f'{extrato_conta[i]}')
    print(f'Saldo: R${saldo:.2f}')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')


def carregando(msg_1, msg_2):
    from time import sleep
    print(msg_1)
    print('.', end='')
    sleep(1)
    print('.', end='')
    sleep(1)
    print('.')
    sleep(1)
    print(msg_2)


def verificacao_s_ou_n():
    while True:

        verificacao = str(input(f'Deseja realizar outra operação? [S/N]: ')).upper().strip()

        if verificacao not in 'SN':
            print('Opção inválida! Digite S para Sim ou N para Não! ')
        else:
            break
    return verificacao


def menu():
    menu_banco = """ 
    -=-=-=-=-=-= BANCO =-=-=-=-=-=

        [1] Deposito
        [2] Saque
        [3] Extrato
        [4] Criar Usuario
        [5] Crir Conta
        [6] Sair

    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    """
    print(menu_banco)
