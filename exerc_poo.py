# Crie uma classe chamada "Retangulo" que tenha atributos para a largura e altura.
# Adicione um método para calcular a área do retângulo e outro para calcular o perímetro.
# Area = largura * altura, Perimetro = 2 * (largura + altura)

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)
    
retangulo = Retangulo(5, 10)
print("Área:", retangulo.area())

print("Perímetro:", retangulo.perimetro())


# Exercicio 2: Crie uma classe chamada "ContaBancaria" que tenha atributos para o nome do titular, saldo e número da conta.
# Adicione métodos para depositar, sacar e exibir o saldo atual.

class ContaBancaria:
    def __init__(self, titular, numero_conta, saldo=0):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado com sucesso.")
        
    def sacar(self, valor):
        self.saldo -= valor
        print(f"Saque de R${valor} realizado com sucesso.")
        
    def exibir_saldo(self):
        return f"Saldo atual: R${self.saldo}"
    
conta = ContaBancaria("Ryan", "12345-6", 1000)
conta.depositar(500)
conta.sacar(200)
print(conta.exibir_saldo())