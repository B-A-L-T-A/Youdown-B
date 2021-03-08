from pytube import YouTube

RED = '\033[31m'
WHITE = '\033[37m'

print("\n\n◈ ━━━━━━━━━━ ◆ ━━━━━━━━━━ ◈")
print(RED+ "╔═╦╗   ╔══╗          ╔══╗")
print("╚╗║╠═╦╦╬╗╗╠═╦╦╦╦═╦╦══╣╔╗║")
print("╔╩╗║╬║║╠╩╝║╬║║║║║║╠══╣╔╗║")
print("╚══╩═╩═╩══╩═╩══╩╩═╝  ╚══╝")

print("-Programado por:", WHITE+"Balta\n")

print("1)Descargar Video\n"
      "2)Salir")

opcion = int(input(RED+"-> Seleccione: "))

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
