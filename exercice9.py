players = {
    "Nil": {"level": 10, "points": 3000},
    "Enzo": {"level": 8, "points": 5000},
    "Edgar": {"level": 15, "points": 1000},
}

player = input("[+] Enter a player name: ")
if players.get(player) != None:

    points = players[player]["points"]
    level = players[player]["level"]
    
    print(f"{player} is level {players[player]["level"]}")

    while points >= 2500:
        points -= 2500
        level += 1
        print(f"[[ LEVEL UP ]] {player} leveled up to level {level}")
