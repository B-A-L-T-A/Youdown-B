from pytube import YouTube
from tqdm import tqdm
import time
from colorama import init, Fore
import os

loop = tqdm(total = 50000, position=0, leave=False)
for k in range(50000):
    loop.set_description('Ejecutando script'.format(k))
    loop.update(1)
loop.close()

os.system("clear")

while True:
    print(Fore.YELLOW + "\n◈ ━━━━━━━━━━ ◆ ━━━━━━━━━━ ◈")
    print(Fore.MAGENTA + "╔═╦╗   ╔══╗          ╔══╗")
    print(Fore.BLUE + "╚╗║╠═╦╦╬╗╗╠═╦╦╦╦═╦╦══╣╔╗║")
    print(Fore.GREEN + "╔╩╗║╬║║╠╩╝║╬║║║║║║╠══╣╔╗║")
    print(Fore.RED + "╚══╩═╩═╩══╩═╩══╩╩═╝  ╚══╝")

    print(Fore.YELLOW + "C", end="")
    print(Fore.GREEN + "o", end="")
    print(Fore.BLUE + "d", end="")
    print(Fore.RED + "e", end="")
    print(Fore.CYAN + "d ", end="")
    print(Fore.MAGENTA + "b", end="")
    print(Fore.WHITE + "y ", end="")
    print(Fore.YELLOW + "B", end="")
    print(Fore.RED + "a", end="")
    print(Fore.YELLOW + "l", end="")
    print(Fore.GREEN + "t", end="")
    print(Fore.MAGENTA + "a", end="")

    url = input(Fore.YELLOW + "\n>>> Enter the URL of the video: ")
    print("\n(･ิᴗ･ิ)", "Downloading Video...")
    YouTube(url).streams.get_highest_resolution().download()
    YouTube(url).streams.first().download()
    print("\n( ^-^)/", "¡Your video has been downloaded successfully!")
    time.sleep(4)
