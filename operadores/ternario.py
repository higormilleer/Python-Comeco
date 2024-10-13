mae_nao_deixou = False
grana = 100

status = "Em casa" if mae_nao_deixou or grana <= 100 else "Uhuu"

print(status)

print(f"O status é: {status}")