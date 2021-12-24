from saldo import Saldo
sald = Saldo()
class Deposito:


    def depositar(self):
        saldoDep = float(input('digite o valor de seu deposito: '))

        if saldoDep >= 10:
            sald.saldo += saldoDep
            sald.limite += saldoDep
            sald.saldoAtual()

        else:
            print('Deposite um valor mais alto')

