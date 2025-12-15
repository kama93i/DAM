# 8 - Gestor de carteras cripto

wallet = {
    "BTC": 0.01,
    "ETH": 1.0023,
    "SOL": 5.3,
}

coin = input("[+] What coin do you want to modify: ")
value = float(input("[+] Value to add: "))

if wallet.get(coin) != None:
    wallet[coin] += value

print(wallet)