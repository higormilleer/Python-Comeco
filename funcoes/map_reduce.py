from functools import reduce

def soma_nota(delta):
    def calc(nota):
        return nota + delta
    return calc

notas = [6.4, 7.2, 5.4, 8.4]

notas_finais_1  = map(soma_nota(1.5), notas)
notas_finais_2  = map(soma_nota(1.6), notas)

notas_finais = list(notas_finais_1)
notas_finais = list(notas_finais_2)

total=0

for n in notas:
    total+=n

print(total)

def soma(a,b):
    return a+b

total = reduce(soma,notas,0) 

print(total)

print(notas_finais)

#for i, nota in enumerate(notas):
#    notas[i] = nota+1,5

#for i in range(len(notas)):
#    notas[i] = notas[i]+1.5