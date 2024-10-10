from functools import reduce

alunos = [
    {"nome":"Ana", "nota": 7.2},
    {"nome":"Higor", "nota": 8.1},
    {"nome":"Claudia", "nota": 8.7},
    {"nome":"Pedro", "nota": 6.4},
    {"nome":"Rafael", "nota": 6.7},
]

alunos_aprovado = lambda aluno: aluno["nota"] >=7
#alunos_honra = lambda aluno: aluno["nota"] >=9

alunos_aprovados = filter(alunos_aprovado, alunos)
alunos_aprovados = list(alunos_aprovados)

obter_nota = lambda aluno: aluno["nota"]
somar = lambda a,b: a+b

nota_aluno_aprovado = map(obter_nota, alunos_aprovados)
nota_aluno_aprovado = list(nota_aluno_aprovado)

total = reduce(somar,nota_aluno_aprovado,0)

#print(alunos_aprovados)
#print(obter_nota(alunos[2]))
#print(nota_aluno_aprovado)
print(total/len(nota_aluno_aprovado))