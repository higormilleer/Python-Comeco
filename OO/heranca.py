class Carro:
    def __init__(self):
        self.__velocidade = 0

    @property
    def velocidade(self):
        return self.velocidade

    def acelerar(self):
        self.__velocidade+=5
        return self.__velocidade
    
    def frear(self):
        self.__velocidade -= 5
        return self.__velocidade

class Uno(Carro):
    pass

class Ferrari(Carro):
    def acelerar(self):
        super().acelerar()
        return super().acelerar()
    def turbo(self):
        self._Carro__velocidade += 30
        return f"Modo Turbo ativado! Velocidade: {self._Carro__velocidade} km/h"

c1 = Ferrari()
print(c1.acelerar())
print(c1.acelerar())
print(c1.acelerar())
print(c1.turbo())
print(c1.frear())
print(c1.frear())
print(c1.frear())