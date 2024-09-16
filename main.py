class BancoDigital:
    def __init__(self):
        self.saldo = 0.0
        self.movimentacoes = []
        self.saques_realizados = 0
        self.limite_saques_diarios = 3
        self.limite_saque_valor = 500.0

    def depositar(self, valor):
        self.saldo += valor
        self.movimentacoes.append(f"Depósito: R$ {valor:.2f}")

    def sacar(self, valor):
        if self.saques_realizados >= self.limite_saques_diarios:
            return "Limite de saques diários atingido."
        if valor > self.limite_saque_valor:
            return f"Saque excede o limite de R$ {self.limite_saque_valor:.2f} por operação."
        if valor > self.saldo:
            return "Saldo insuficiente para realizar o saque."
        
        self.saldo -= valor
        self.movimentacoes.append(f"Saque: R$ {valor:.2f}")
        self.saques_realizados += 1
        return f"Saque de R$ {valor:.2f} realizado com sucesso."

    def extrato(self):
        if not self.movimentacoes:
            return "Não foram realizadas movimentações."
        extrato = "\n".join(self.movimentacoes)
        extrato += f"\nSaldo atual: R$ {self.saldo:.2f}"
        return extrato

