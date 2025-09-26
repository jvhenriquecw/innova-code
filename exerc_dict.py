# Crie um dicionário chamado aluno com as informações: nome = "Maria", idade = 17 e notas = [8.5, 7.0, 9.0]. Depois, tente acessar uma informação chamada "turma". Se ela não existir, coloque "3ºB". Por fim, mude a idade para 18.

aluno  = dict(nome="Maria", idade=17, notas=[8.5, 7.0, 9.0])

turma = aluno.get("turma", "3ºB")
print("Turma:", turma)

aluno["idade"] = 18
print("Idade atualizada:", aluno.get("idade"))

# Com o dicionário {"Ana": 8.0, "Pedro": 5.5, "João": 6.0, "Carla": 9.0, "Bia": 4.5}, crie outro dicionário que guarde apenas os alunos que têm nota maior ou igual a 6.

notas = {"Ana": 8.0, "Pedro": 5.5, "João": 6.0, "Carla": 9.0, "Bia": 4.5}

alunos_aprovados = {nome: nota for nome, nota in notas.items() if nota >= 6}

print("Alunos aprovados:", alunos_aprovados)

# Com o dicionário {"Brasil": "Brasília", "França": "Paris", "Japão": "Tóquio"}, monte outro dicionário em que a chave seja a capital e o valor seja o país.

paises = {"Brasil": "Brasília", "França": "Paris", "Japão": "Tóquio"}

capitais = {capital: pais for pais, capital in paises.items()}

print("Capitais invertidas:", capitais)

# Com o dicionário {"Ana": [7, 8, 9], "Pedro": [5, 6, 7], "João": [9, 9, 10]}, calcule a média das notas de cada aluno e faça um novo dicionário. Depois, crie outro guardando apenas os alunos com média maior ou igual a 7.

notas_alunos = {"Ana": [7, 8, 9], "Pedro": [5, 6, 7], "João": [8, 9, 10]}

medias = {nome: sum(notas)/len(notas) for nome, notas in notas_alunos.items()}

print("Médias dos alunos:", medias)

alunos_aprovados_media = {nome: media for nome, media in medias.items() if media >= 7}

print("Alunos com média maior ou igual a 7:", alunos_aprovados_media)

