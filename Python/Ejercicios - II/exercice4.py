# 4 - Registro de peso semanal

weight: list[float] = []
for i in range(5):
    w = float(input(f"[+] Insert your weight nº {i+1}: "))
    weight.append(w)

average = sum(weight) / len(weight)
print("The average weight is: ", average)