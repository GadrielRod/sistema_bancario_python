from saldo import Saldo
from deposito import Deposito

saldo = Saldo()
deposito = Deposito()

class Menu:

    def escolher(self):

            print('Escolha uma das operações abaixo: \n'
                  ' 1 - depositar '
                  ' 2 - saldo \n'
                  ' 3 - tranferencia '
                  ' 4 - saque \n'
                  ' 5 - emprestimo '
                  ' 6 - sair ')

            opcao: int = int
            while opcao != 6:
                opcao = int(input('digite uma das opções abaixo: '))
                if opcao == 1:
                    (
                        deposito.depositar()
                    )
                elif opcao == 2:
                    (
                        saldo.saldoAtual()
                    )
                elif opcao == 3:
                    (
                    print('Você escolheu a opcão 3')
                    )
                elif opcao == 6:
                    (
                    print('Obrigado volte sempre')
                    )

                else:
                    print('opcao invalida')


