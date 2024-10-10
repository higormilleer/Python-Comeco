class Produto:
    def __init__(self,nome, preco = 1.99, desc=0):
        self.nome = nome
        self.__preco = preco
        self.desc = desc

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco

    @property #faz acessar o def como se fosse um atributo
    def preco_final(self):
        return (1-self.desc) * self.preco    

p1 = Produto("Caneta", 5.99, 0.10)
p2 = Produto("Caderno", 12.99, 0.10)

p1.preco = -70
p2.preco = - 2

print(p1.nome,p1.preco, p1.desc, p1.preco_final)
print(p2.nome, p2.preco, p2.desc, p2.preco_final)