#Dicionarios

#Explicação:
# Armazenam pares de chave e valor
# Chave: Identificador 
# Valor: Informação 

# Código:

# Exemplo 1
pessoa = {
    'nome':'Ryan',
    'idade': 14,
    'altura': 1.75,
    'peso': 60,
    'endereco':[{'rua':'avenida rio branco', 'numero':43}]
}

print(pessoa['nome'], '\n')

# Exemplo 2
carro = {
    'marca': 'Toyota',
    'modelo': 'Corolla',
    'ano': 2020,
    'caracteristicas': {
        'cor': 'Prata',
        'motor': '2.0L',
        'combustivel': 'Gasolina'
    }
}

print(carro['caracteristicas']['cor'],'\n')

# Metodos Uteis

#Explicação:
# Facilita a manipulação de dados

# Código:
print(len(pessoa), '\n') # Quantidade de itens no dicionario
print(pessoa.get('nome', 'não existe'), '\n') # Acessa o valor da chave especificada
print(pessoa.values(), '\n') # Retorna todos os valores do dicionario
print(pessoa.keys(), '\n') # Retorna todas as chaves do dicionario
print(pessoa.items(), '\n') # Retorna todos os pares chave-valor

for chave, valor in pessoa.items(): 
    print(f'Chave: {chave}, Valor: {valor}')

dados_pessoa = {
    'cpf': '123.456.789-00',
    'rg': '12.345.678-9'
}

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)

#List Comprehension

#Explicação:
# Sintaxe mais enxuta para criar listas
# Pode incluir condicionais e loops

# Código:
lista1 = []
for numero in range(10):
    lista1.append(numero)

print(lista1)

lista2 = [numero * 2 for numero in range(10)]
print(lista2)

pares = [numero for numero in range(10) if numero % 2 == 0]
print(pares)

produtos = [
    {'produto1': 'camiseta', 'preco': 50},
    {'produto2': 'calça', 'preco': 150},
    {'produto3': 'tenis', 'preco': 200}
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.01}
    if produto['preco'] > 100 else {**produto}
    for produto in produtos 
    # Aumenta 1% no preco se for maior que 100
]

print(*novos_produtos, sep='\n')


# Exercicio 
perguntas = [
    {'pergunta': 'Qual é a capital da França?',
    'opcoes': ['Paris', 'Londres', 'Berlim', 'Madrid'],
    'resposta_correta': 'Paris'
    },
    {'pergunta': 'Qual é o maior planeta do sistema solar?',
    'opcoes': ['Terra', 'Júpiter', 'Saturno', 'Marte'],
    'resposta_correta': 'Júpiter'
    },  
]

for item in perguntas:
    print(item['pergunta'])
    
    for opcao in item['opcoes']:
        print(f"- {opcao}")
    resposta = input("Digite sua resposta: ")
    
    if resposta == item['resposta_correta']:
        print("Resposta correta!\n")
    else:
        print(f"Resposta incorreta! A resposta correta é: {item['resposta_correta']}\n")
            

# Crie um dicionário chamado aluno com as informações: nome = "Maria", idade = 17 e notas = [8.5, 7.0, 9.0]. Depois, tente acessar uma informação chamada "turma". Se ela não existir, coloque "3ºB". Por fim, mude a idade para 18.

# Com o dicionário {"Ana": 8.0, "Pedro": 5.5, "João": 6.0, "Carla": 9.0, "Bia": 4.5}, crie outro dicionário que guarde apenas os alunos que têm nota maior ou igual a 6.

# Com o dicionário {"Brasil": "Brasília", "França": "Paris", "Japão": "Tóquio"}, monte outro dicionário em que a chave seja a capital e o valor seja o país.

# Com o dicionário {"Ana": [7, 8, 9], "Pedro": [5, 6, 7], "João": [9, 9, 10]}, calcule a média das notas de cada aluno e faça um novo dicionário. Depois, crie outro guardando apenas os alunos com média maior ou igual a 7.
        















