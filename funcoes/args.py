def soma(*nums):
    total = 0
    for n in nums:
        total += n
    return total

def resultado_final(**kwargs):
    status = "Aprovado" if kwargs["nota"] >=7 else "Reprovado"
    return f"{kwargs["nome"]} foi {status}"
    

def resultado_final(**kwargs):
    nota = kwargs.get("nota", 0)
    comportado = kwargs.get("comportado", True)
    nome = kwargs.get("nome", "Aluno")
    
    status = "Aprovado" if nota >= 7 else "Reprovado"
    
    if not comportado:
        status = "Reprovado por comportamento"
    
    return f"{nome} foi {status}, com média {nota}"
