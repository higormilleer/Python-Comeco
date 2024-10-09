def saudacao(nome = "Pessoa", idade = 20): #paremetro padrao
    print(f"Bom dia {nome}! Vc nem parece ter {idade} anos")

def saudacao():  #sobreescrever
    print("Bom dia")

def soma_e_multi(a,b,x):
    return a+b*x

if __name__ == "__main__":
    saudacao(nome = "Ana", idade = 20)
