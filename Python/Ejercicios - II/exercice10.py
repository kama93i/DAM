artists = [
    {"name": "Quepedo", "genere": "Urban"},
    {"name": "Saiko", "genere": "Urban"},
    {"name": "Urion", "genere": "R&B"},
]

for i, artist in enumerate(artists):
    print(f"{i+1}. {artist["name"]}")

genere = input("[+] Enter a genere to find similar artists: ")

for artist in artists:
    if artist["genere"] == genere:
        print(f"{artist["name"]} matches generes!")
else:
    print("Playlist created")