for x in range(5):
    if x % 2 == 0:
        print(f"{x} é par", end=" ")
    else:
        print(f"{x} é ímpar", end=" ")

soma = 0

for y in range(1, 6):
    soma += y
    print(f"Soma atual: {soma}", end=" ")

for i in range(1,100, 5):
    print(i,end = " ")

for i in range(30, 0, -3):
    print(i,end = " ")

nums = [2,4,6,8]

for n in nums:
    print(n, end = " ")

texto = "Python"

for letra in texto:
    print(letra, end = " ")

for n in {1,2,3,4,4,4}:
    print(n, end = " ")

produto = {
    "nome": "Higor",
    "Nota": "7.0",
    "trabalho": 0.5
}

for atrib in produto:
    print(atrib,"-->", produto[atrib])

for atrib,valor in produto.items():
    print(atrib,"-->", valor)

for valor in produto.values():
    print(valor,end = " ")

for atrib in produto.keys():
    print(atrib,end = " ")