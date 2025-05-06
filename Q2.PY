class ContaCorrente:
    def __init__(self, nomeCliente, saldoInicial):
        self.cliente = nomeCliente
        self.saldo = saldoInicial

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False