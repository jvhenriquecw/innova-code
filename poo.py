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