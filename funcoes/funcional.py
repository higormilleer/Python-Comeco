def soma(a,b):
    return a+b

def sub(a,b):
    return a-b


somar = soma
print(somar(2,3))

def operacao_aritmetica(fn,op1,op2):
    return fn(op1,op2)

result = operacao_aritmetica(soma,13,48)
print(result)

result = operacao_aritmetica(sub,13,48)
print(result)

def soma_parcial(a):
    #proc pesado - 10s
    #proc pesado - 10s
    #proc pesado - 40s
    def concluir_soma(b):
        return a + b #10s
    return concluir_soma

#r1 = soma_total(1,2) -> 1m10s
#r2 = soma_total(1,3) -> 1m10s
#r3 = soma_total(1,4) -> 1m10s

soma_1 = soma_parcial(1) #1m
r1 = soma_1(2)
r2 = soma_1(3)
r3 = soma_1(4)

resultado_final = soma_parcial(10)(12)
print(resultado_final,r1,r2,r3 )
