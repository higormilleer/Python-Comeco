pessoas = ["Gui", "Rebeca"]
adj = ["Sapeca", "Inteligente"]

for p in pessoas:
    for a in adj:
        print(f"{p} é {a}!")

print("")

for i in [1,2,3]:
    pass

print("")

for i in range(1,11):
    if i % 2 == 1:
        continue
    print(i, end = " ")

print("")

#Decrescente de 10 a 1 mostrando qual e divisivel por 3
for i in range(10, 0, -1):  
    if i % 3 == 0:
        print(f"{i} é divisível por 3")
    else:
        print(i, end=" ")

print("")

for i in range(1,11):
    if i == 5:
        break
    print(i, end = " ")
    
print("Fim")