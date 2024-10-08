nota = float(input("Informe a nota do aluno: "))
comportado = True if input("Comportado(y/n): ") == "y" else False


if nota>= 9 and comportado: 
    print("Duas palavras: Para bens! ")
    print("Quadro de Honra" )
elif nota >=7:
    print("Aprovado! ")
elif nota >=5:
    print("Recuperacao! ")
else:
    print("Reprovado! ")

print(nota)