lockdown = False
grana = 30

status = "Em casa" if lockdown or grana <= 100 else "Uhuu"

print(status)

print(f"O status é: {status}")