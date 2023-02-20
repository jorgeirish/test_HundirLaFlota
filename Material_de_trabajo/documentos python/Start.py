import numpy as np
import LockIn_machine
import LockIn_player
import Disparar_player
import Disparar_machine


inicio = input("Para jugar pulsa P, para salir pulsa O")

if inicio.lower() == "p":
    print(LockIn_player.LockIn())

    cambiar = input("Para comfirmar pulsa A. Si no te gustan los barcos puedes cambiar pulsando N")

    if cambiar.lower() == "a":
        print("Este es el mapa rival", Disparar_machine.disparo)
    elif cambiar.lower() == "n":
        print(LockIn_player.LockIn())

else:
    print("Adios")
