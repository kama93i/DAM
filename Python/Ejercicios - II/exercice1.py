# 1- Playlsit Personalizada

playlist: list[str] = []

for i in range(3):
    playlist.append(input(f"[+] Ingrese la cancion numero {i+1}: "))

print("Tu playlist esta lista: ", playlist)