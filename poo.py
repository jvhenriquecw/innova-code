# Classes
# Classe: Molde para criar objetos
# Objeto: Instância de uma classe
# Atributos: Características do objeto
# Métodos: Funções dentro da classe que definem comportamentos do objeto

#Self: Referência ao próprio objeto

# Código:
class Pessoa:
    pass

p1 = Pessoa()
p1.nome = "Ryan"
p1.idade = 16

p2 = Pessoa()
p2.nome = "Jv"
p2.idade = 15

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)

# Exemplo 1
class Pessoa:
    def __init__(self, nome, idade): # Construtor
        self.nome = nome  # Atributo
        self.idade = idade  # Atributo

    def apresentar(self):  # Método
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."
#Exemplo 2
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        return f"{self.marca} {self.modelo}, Ano: {self.ano}"
    
meu_carro = Carro("Toyota", "Corolla", 2020)


# Exercicio: Crie uma classe chamada "Retangulo" que tenha atributos para a largura e altura.
# Adicione um método para calcular a área do retângulo e outro para calcular o perímetro.
# Area = largura * altura, Perimetro = 2 * (largura + altura)

# Exercicio 2: Crie uma classe chamada "ContaBancaria" que tenha atributos para o nome do titular, saldo e número da conta.
# Adicione métodos para depositar, sacar e exibir o saldo atual.

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