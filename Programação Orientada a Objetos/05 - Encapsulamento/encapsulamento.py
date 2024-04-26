class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor


conta = Conta(1000)
conta.depositar(500) # 1500 (saldo inicial + 500)
print(conta._saldo)  # 1000 (saldo inicial)