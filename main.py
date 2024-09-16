class BancoDigital:
    def __init__(self):
        self.saldo = 0.0
        self.movimentacoes = []
        self.saques_realizados = 0
        self.limite_saques_diarios = 3
        self.limite_saque_valor = 500.0

    def depositar(self, valor):
        """Realiza um depósito na conta."""
        self.saldo += valor
        self.movimentacoes.append(f"Depósito: R$ {valor:.2f}")
        return f"Depósito de R$ {valor:.2f} realizado com sucesso."

    def pode_sacar(self, valor):
        """Verifica se o saque pode ser realizado com base nas condições de saldo e limite."""
        if self.saques_realizados >= self.limite_saques_diarios:
            return False, "Limite de saques diários atingido."
        if valor > self.limite_saque_valor:
            return False, f"Saque excede o limite de R$ {self.limite_saque_valor:.2f} por operação."
        if valor > self.saldo:
            return False, "Saldo insuficiente para realizar o saque."
        return True, ""

    def sacar(self, valor):
        """Realiza o saque se todas as condições forem atendidas."""
        permitido, mensagem = self.pode_sacar(valor)
        if not permitido:
            return mensagem

        self.saldo -= valor
        self.movimentacoes.append(f"Saque: R$ {valor:.2f}")
        self.saques_realizados += 1
        return f"Saque de R$ {valor:.2f} realizado com sucesso."

    def extrato(self):
        """Exibe o extrato de todas as movimentações realizadas na conta."""
        if not self.movimentacoes:
            return "Não foram realizadas movimentações."
        extrato = "\n".join(self.movimentacoes)
        extrato += f"\nSaldo atual: R$ {self.saldo:.2f}"
        return extrato


# Funções gerais para operações

def realizar_deposito(banco, valor):
    """Função para realizar um depósito."""
    return banco.depositar(valor)

def realizar_saque(banco, valor):
    """Função para realizar um saque."""
    return banco.sacar(valor)

def exibir_extrato(banco):
    """Função para exibir o extrato."""
    return banco.extrato()