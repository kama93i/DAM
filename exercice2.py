# 2- Modificando la playlist

playlist: list[str] = ["Bad bunny", "Quevedo", "Saiko", "Shakira"] 

idx = int(input("[+] What index do you want to remove: "))
if len(playlist) >= idx:
    playlist.pop(idx)

print("The list is now: ", playlist)