# 6 - Inventario deportivo
inventory = {
    "mancuernas": 3,
    "pesas": 20,
    "colchonetas": 1,
}

print(inventory)
key = input("[+] Insert an inventory item: ")
if inventory.get(key) != None:
    print(f"{key} - {inventory[key]}")
else: print("Key not in inventory")
