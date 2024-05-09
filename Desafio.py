from time import sleep


def carregando(msg_1, msg_2):
    print(msg_1)
    print('.', end='')
    sleep(1)
    print('.', end='')
    sleep(1)
    print('.')
    sleep(1)
    print(msg_2)


menu = """ 
-=-=-=-=-=-= BANCO =-=-=-=-=-=

    [1] Deposito
    [2] Saque
    [3] Extrato
    [4] Sair
    
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
"""

saldo = 0
limite_por_saque = 500
extrato = []
numero_de_saques = 0
LIMITE_DE_SAQUES = 3


while True:

    try:
        print(menu)
        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:

                while True:
                    try:
                        valor_a_depositar = int(input('Quanto você deseja depositar?: '))

                        if valor_a_depositar <= 0:
                            print('Não é possivel depositar esse tipo de valor!\nTente um valor inteiro acima de 0!')

                        else:
                            saldo += valor_a_depositar
                            extrato.append('Deposito')
                            extrato.append(f'    + R${valor_a_depositar}')
                            carregando('Fazendo deposito!', 'Valor depositado com sucesso!')
                            break

                    except ValueError:
                        print('Valor digitado incorreto!, Aceitamos apenas valores inteiros!')

        elif opcao == 2:
            while True:
                try:
                    valor_a_sacar = int(input('Quanto você deseja sacar?: '))

                    if saldo == 0:
                        print('Não foi possivel realizar o saque!\nVocê não tem valores disponiveis para sacar!')
                        print(f'Seu saldo atual é de R${saldo:.2f}')
                        break

                    elif valor_a_sacar > saldo:
                        carregando('Fazendo saque!',
                                   'Não foi possivel realizar o saque!\nO valor que deseja sacar e menor do que seu saldo!'
                                   )
                        print(f'Seu saldo atual é de R${saldo:.2f}')

                    elif valor_a_sacar > limite_por_saque:
                        print(f'Não foi possivel realizar o saque!\nO valor limite por saque é de R${limite_por_saque:.2f}!')

                    elif LIMITE_DE_SAQUES == 0:
                        carregando('Fazendo saque!', f'Não foi possivel realizar o saque!\nO limite de saque diario excedeu!')
                        print('Tente novamente amanhã!')
                        break

                    else:
                        saldo -= valor_a_sacar
                        LIMITE_DE_SAQUES -= 1
                        extrato.append('Saque')
                        extrato.append(f'    - R${valor_a_sacar}')
                        carregando('Fazendo saque!', 'Saque realizado com sucesso!')
                        break

                except ValueError:
                    print('Valor digitado incorreto!, Aceitamos apenas valores inteiros!')

        elif opcao == 3:
            carregando('Exibindo extrato', '')
            print('=-=-=-=-=-= EXTRATO =-=-=-=-=-')
            for i in range(0, len(extrato)):
                print(f'{extrato[i]}')
            print(f'Saldo: R${saldo:.2f}')
            print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

        elif opcao == 4:
            carregando('Saindo do sistema!', 'Obrigado por ultilizar nosso sistema, até a proxima :)')
            break
        else:
            print('Opção invalida, escolha uma das opções acima! ')

        verificacao = ''

        while True:

            verificacao = str(input(f'Deseja realizar outra operação? [S/N]: ')).upper().strip()

            if verificacao not in 'SN':
                print('Opção inválida! Digite S para Sim ou N para Não! ')
            else:
                break

        if verificacao == 'N':
            carregando('Saindo do sistema!', 'Obrigado por ultilizar nosso sistema, até a proxima :)')
            break
    except ValueError:
        print('Valor digitado incorreto!\nEscolha uma das opções abaixo!')
