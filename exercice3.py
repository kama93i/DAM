# 3 - Plan semanal de gimnasio

rutine: list[str] = ["Piernas", "Pecho", "Espalda", "Descanso", "Cardio", "Descanso", "Pecho"]
idx = int(input("[+] Select a day of the week (1-7): "))

print("The rutine is ", rutine[idx-1])