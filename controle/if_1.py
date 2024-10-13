nota = float(input("Informe a nota do estudante: "))
comportado = input("O aluno foi comportado (s/n)? ").lower() == 's'


#modifiquei para que a mensagem mudasse dependendo do comportamento do aluno
if nota >= 9 and comportado:
    print("Excelente! Duas palavras: Para bens!")
    print("Será destaque no Quadro de Honra.")
elif nota >= 7 and comportado:
    print("Aprovado, Comportamento bom.")
elif nota >= 7:
    print("Aprovado, melhorar o comportamento.")
elif nota >= 5:
    print("Recuperação.")
else:
    if comportado:
        print("Reprovado, comportamento foi bom.")
    else:
        print("Reprovado, melhorar o comportamento.")

print(f"Nota final: {nota}")
