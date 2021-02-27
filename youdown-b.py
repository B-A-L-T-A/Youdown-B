from pytube import YouTube
from tqdm import tqdm

loop = tqdm(total = 30000, position=0, leave=False)
for k in range(30000):
    loop.set_description('Abriendo Programa'.format(k))
    loop.update(1)
loop.close()

RED = '\033[31m'
WHITE = '\033[37m'

print("\n\n◈ ━━━━━━━━━━ ◆ ━━━━━━━━━━ ◈")
print(RED+ "╔═╦╗   ╔══╗          ╔══╗")
print("╚╗║╠═╦╦╬╗╗╠═╦╦╦╦═╦╦══╣╔╗║")
print("╔╩╗║╬║║╠╩╝║╬║║║║║║╠══╣╔╗║")
print("╚══╩═╩═╩══╩═╩══╩╩═╝  ╚══╝")

print("-Programado por:", WHITE+"Balta\n")

print("1)Descargar Video\n"
      "3)Salir")

opcion = int(input(RED+"-> Selecione: "))

if opcion == 1:
    urlv = input(RED + "\n-> Introduzca la URL del video: ")
    print(WHITE + "\n(･ิᴗ･ิ)", RED + "Descargando Video...")
    YouTube(urlv).streams.get_highest_resolution().download()
    YouTube(urlv).streams.first().download()
    print(WHITE + "\n( ^-^)/", RED + "¡Su video se ha descargado satisfactoriamente!")

elif opcion == 2:
    exit()

else:
    print("(•ิ_•ิ) Algo Anda mal")
