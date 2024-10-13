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


celsius_para_fahrenheit = lambda c: (c * 9/5) + 32

temperaturas_celsius = [-5, 0, 10, 20, 30, 35, 40]

temperaturas_fahrenheit = map(celsius_para_fahrenheit, temperaturas_celsius)

temperaturas_fahrenheit = list(temperaturas_fahrenheit)

verificar_temperatura = lambda temp: "congelando" if temp < 32 else "muito quente" if temp > 95 else "normal"

print("Temperaturas em Celsius:", temperaturas_celsius)
print("Temperaturas em Fahrenheit:", temperaturas_fahrenheit)
print("Status das temperaturas:", verificar_temperatura)
