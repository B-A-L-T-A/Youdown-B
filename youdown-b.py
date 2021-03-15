from colorama import Fore, Style
import pafy
import os

os.system("clear")

print(Fore.LIGHTYELLOW_EX + "\n◈ ━━━━━━━━━━ ◆ ━━━━━━━━━━ ◈")
print( "╔═╦╗   ╔══╗          ╔══╗")
print("╚╗║╠═╦╦╬╗╗╠═╦╦╦╦═╦╦══╣╔╗║")
print("╔╩╗║╬║║╠╩╝║╬║║║║║║╠══╣╔╗║")
print("╚══╩═╩═╩══╩═╩══╩╩═╝  ╚══╝")

print(Fore.YELLOW + "1", end="")
print(Fore.GREEN + ") ", end="")
print(Fore.BLUE + "D", end="")
print(Fore.RED + "e", end="")
print(Fore.CYAN + "s", end="")
print(Fore.MAGENTA + "c", end="")
print(Fore.WHITE + "a", end="")
print(Fore.YELLOW + "r", end="")
print(Fore.RED + "g", end="")
print(Fore.YELLOW + "a", end="")
print(Fore.GREEN + "r", end="")
print(Fore.BLUE + " V", end="")
print(Fore.YELLOW + "i", end="")
print(Fore.GREEN + "d", end="")
print(Fore.YELLOW + "e", end="")
print(Fore.GREEN + "o")
print(Fore.BLUE + "2", end="")
print(Fore.RED + ")", end="")
print(Fore.CYAN + "D", end="")
print(Fore.MAGENTA + "e", end="")
print(Fore.WHITE + "s", end="")
print(Fore.YELLOW + "c", end="")
print(Fore.RED + "a", end="")
print(Fore.YELLOW + "r", end="")
print(Fore.GREEN + "g", end="")
print(Fore.BLUE + "a", end="")
print(Fore.YELLOW + "r ", end="")
print(Fore.GREEN + "A", end="")
print(Fore.CYAN + "u", end="")
print(Fore.MAGENTA + "d", end="")
print(Fore.WHITE + "i", end="")
print(Fore.YELLOW + "o")
print(Fore.WHITE + "3", end="")
print(Fore.YELLOW + ") ", end="")
print(Fore.RED + "S", end="")
print(Fore.YELLOW + "a", end="")
print(Fore.GREEN + "l", end="")
print(Fore.BLUE + "i", end="")
print(Fore.YELLOW + "r", end="")
selec = input("Seleccione: ")

if selec == "1":
    # URL
    download_url = input(Style.BRIGHT + Fore.RED + "URL: " + Style.NORMAL + Fore.WHITE)
    video = pafy.new(download_url)

    streams = video.streams

    for i in streams:
        print(i)

    # Mejor resolucion
    best = video.getbest()
    print(best.resolution, best.extension)

    # Descarga - Directorio
    best.download(filepath="video")
    print(Fore.RED + "Video descargado correctamente!")

elif selec == "2":
    download_url = input(Style.BRIGHT + Fore.RED + "URL: " + Style.NORMAL + Fore.WHITE)
    video = pafy.new(download_url)

    audiostreams = video.audiostreams
    for i in audiostreams:
        print(i.bitrate, i.extension, i.get_filesize())

    audiostreams[1].download()
    print(Fore.RED + "Audio descargado correctamente!")

else:
    exit()
