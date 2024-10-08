x=10
while x:
    print(x) #melhor o proprio for, while apenas para qtde indeterminada
    x-=1

print("Fim")

total = 0
qtde = 0
nota = 0

while nota != -1:
    nota = float(input("Informe a nota ou -1 para sair: "))
    if nota!=-1: 
        qtde += 1
        total +=nota


print(f"A media da turma é: {total/qtde}")
