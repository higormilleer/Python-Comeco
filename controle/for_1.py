for i in range(10):
    print(i,end = " ")

for i in range(1,11):
    print(i,end = " ")


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
    "nome": "Caneta",
    "preco": "8.80",
    "desconto": 0.5
}

for atrib in produto:
    print(atrib,"-->", produto[atrib])

for atrib,valor in produto.items():
    print(atrib,"-->", valor)

for valor in produto.values():
    print(valor,end = " ")

for atrib in produto.keys():
    print(atrib,end = " ")