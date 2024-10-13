x=10
while x:
    print(x) #melhor o proprio for, while apenas para qtde indeterminada
    x-=1

#verificar se e par ou impar com while
y = 15
while y > 0:
    if y % 2 == 0:
        print(f"{y} é par!")
    else:
        print(f"{y} é ímpar!")
    y -= 1

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
