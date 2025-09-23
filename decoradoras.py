# *args e **kwargs

#Explicação:
# args: Argumentos posicionais
# kwargs: Argumentos nomeados
# Permitem flexibilidade na passagem de argumentos
# Úteis para funções que aceitam número variável de argumentos

# Código:
def funcao_exemplo(*args, **kwargs):
    print("Argumentos posicionais (args):", args)
    print("Argumentos nomeados (kwargs):", kwargs)

funcao_exemplo(1, 2, 3, nome='Ryan', idade=14)

# Decoradores

#Explicação:
# Funções que modificam o comportamento de outras funções


# Código:
#Exemplo 1
def decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes da função")
        resultado = func(*args, **kwargs)
        print("Depois da função")
        return resultado
    return wrapper

@decorador
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Ryan")

#Exemplo 2
def inverte_string(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return resultado[::-1]
    return wrapper

@inverte_string
def obter_string(string):
    if not isinstance(string, str):
        raise TypeError("O parâmetro deve ser uma string")
    return string

print(obter_string("Python"))   
print(obter_string(123))  # Levanta TypeError   

# Exercicio

# Crie um decorador que multiplica o resultado de uma função por 2.

def multiplica_por_dois(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return resultado * 2
    return wrapper 

@multiplica_por_dois
def retorna_numero(num):
    return num


# Guard Clause

#Explicação:
# Técnica para simplificar funções removendo aninhamentos desnecessários
# Melhora a legibilidade do código
# Utiliza retornos antecipados para casos especiais
# Evita múltiplos níveis de indentação

# Código:

# Exemplo 1
# Sem Guard Clause
def verifica_idade_sem_gd(idade):
    if idade >= 0:
        if idade < 18:
            return "Menor de idade"
        else:
            return "Maior de idade"
    else:
        return "Idade inválida"

# Com Guard Clause
def verifica_idade_com_gd(idade):
    if idade < 0:
        return "Idade inválida"
    if idade < 18:
        return "Menor de idade"
    return "Maior de idade"

# Exemplo 2
# Sem Guard Clause
def reservar_quarto(cliente, dias, quartos_disponiveis, limite_cartao):
    if cliente:
        if dias > 0:
            if quartos_disponiveis > 0:
                preco_total = dias * 200
                if limite_cartao >= preco_total:
                    return f"Reserva confirmada para {cliente}, valor R${preco_total:.2f}"
                else:
                    return "Erro: limite do cartão insuficiente."
            else:
                return "Erro: não há quartos disponíveis."
        else:
            return "Erro: número de dias inválido."
    else:
        return "Erro: cliente não informado."

# Com Guard Clause
def reservar_quarto_gc(cliente, dias, quartos_disponiveis, limite_cartao):
    if not cliente:
        return "Erro: cliente não informado."
    if dias <= 0:
        return "Erro: número de dias inválido."
    if quartos_disponiveis <= 0:
        return "Erro: não há quartos disponíveis."
    
    preco_total = dias * 200
    if limite_cartao < preco_total:
        return "Erro: limite do cartão insuficiente."
    
    return f"Reserva confirmada para {cliente}, valor R${preco_total:.2f}"

# Exemplo 3 (Com Dict)
usuarios = {
    "joao": {"nome": "João", "idade": 20, "ativo": True},
    "maria": {"nome": "Maria", "idade": 17, "ativo": False},
    "pedro": {"nome": "Pedro", "idade": 25, "ativo": True},
}


# Sem Guard Clause
def acessar_perfil(username, usuarios):
    if username in usuarios:
        usuario = usuarios[username]
        if usuario["ativo"]:
            if usuario["idade"] >= 18:
                return f"Acesso liberado: {usuario['nome']} (idade {usuario['idade']})"
            else:
                return "Erro: usuário menor de idade."
        else:
            return "Erro: usuário inativo."
    else:
        return "Erro: usuário não encontrado."

# Com Guard Clause
def acessar_perfil(username, usuarios):
    if username not in usuarios:
        return "Erro: usuário não encontrado."
    
    usuario = usuarios[username]
    
    if not usuario["ativo"]:
        return "Erro: usuário inativo."
    
    if usuario["idade"] < 18:
        return "Erro: usuário menor de idade."
    
    return f"Acesso liberado: {usuario['nome']} (idade {usuario['idade']})"



