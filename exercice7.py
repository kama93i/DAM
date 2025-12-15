# 7 - Recomendador nutricional

menu = {
    "pollo": {"proteinas": 27, "calorias": 240},
    "ensalada": {"proteinas": 35, "calorias": 75},
    "pizza": {"proteinas": 30, "calorias": 501},
}

    

key = input("[+] What item do you want: ")
if menu.get(key) != None:
    item = menu[key]
    
    print(item)
    if item["calorias"] > 500:
        print("Comida alta en calorias")

else: print("Key not in inventory")