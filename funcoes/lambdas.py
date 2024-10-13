from functools import reduce

alunos = [
    {"nome":"Yuri", "nota": 8.0},
    {"nome":"Higor", "nota": 9.0},
    {"nome":"Matheus", "nota": 6.0},
    {"nome":"Lucas", "nota": 7.0},
    {"nome":"Luigi", "nota": 4.0},
]

alunos_aprovado = lambda aluno: aluno["nota"] >=7
#alunos_honra = lambda aluno: aluno["nota"] >=9

alunos_aprovados = filter(alunos_aprovado, alunos)
alunos_aprovados = list(alunos_aprovados)

obter_nota = lambda aluno: aluno["nota"]
somar = lambda a,b: a+b

nota_aluno_aprovado = map(obter_nota, alunos_aprovados)
nota_aluno_aprovado = list(nota_aluno_aprovado)

#verifica qual a maior nota dos aprovados
maxima = lambda a, b: a if a > b else b
nota_maxima = reduce(maxima, nota_aluno_aprovado)

total = reduce(somar,nota_aluno_aprovado,0)

#print(alunos_aprovados)
#print(obter_nota(alunos[2]))
#print(nota_aluno_aprovado)
print(nota_maxima)
print(total/len(nota_aluno_aprovado))