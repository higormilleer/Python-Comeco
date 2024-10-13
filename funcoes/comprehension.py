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

#Lista de alunos reprovados
alunos_reprovados = [aluno for aluno in alunos if aluno["nota"] < 7]
nota_aluno_reprovado = [aluno["nota"] for aluno in alunos_reprovados]
total_reprovado = reduce(somar,nota_aluno_aprovado,0)

print(total)
print(total_reprovado)
print(alunos_aprovados)
print(alunos_reprovados)