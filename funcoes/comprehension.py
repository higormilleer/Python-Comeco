from functools import reduce

alunos = [
    {"nome":"Ana", "nota": 7.2},
    {"nome":"Higor", "nota": 8.1},
    {"nome":"Claudia", "nota": 8.7},
    {"nome":"Pedro", "nota": 6.4},
    {"nome":"Rafael", "nota": 6.7},
]

somar = lambda a,b: a+b

alunos_aprovados =[aluno for aluno in alunos if aluno["nota"]>=7]
nota_aluno_aprovado = [aluno["nota"] for aluno in alunos_aprovados]
total = reduce(somar,nota_aluno_aprovado,0)

print(total/len(nota_aluno_aprovado))


total_ponderado = reduce(
    lambda acc, aluno: acc + aluno["nota"] * aluno["peso"], alunos, 0
)

total_pesos = reduce(lambda acc, aluno: acc + aluno["peso"], alunos, 0)

media_ponderada = total_ponderado / total_pesos if total_pesos != 0 else 0

print(f"Média ponderada geral: {media_ponderada:.2f}")