class Contador:
    contador = 0 #atributo de classe

    def inst(self):
        return "Estou bem"

    @classmethod
    def incremento(cls):
        cls.contador += 1
        return cls.contador
    
    @classmethod
    def decremento(cls):
        cls.contador -= 1
        return cls.contador
    
    #reinicia o contador de incremento/decremento
    def reiniciar_contador(cls):
        cls.contador = 0
        return cls.contador
    
    @staticmethod
    def mais_um(n):
        return n+1

c1 = Contador()
print(c1.inst())

print(Contador.incremento())
print(Contador.incremento())
print(Contador.incremento())
print(Contador.decremento())
print(Contador.decremento())
print(Contador.decremento())
print(Contador.mais_um(99))

print(Contador.reiniciar_contador())