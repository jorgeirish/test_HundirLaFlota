import numpy as np
import LockIn_player

"""
Copia tablero de la máquina para jugar sobre él

OPCIONES
-> Si aciertas repites.
-> Si fallas paras de jugar.
-> Si disparas en un sitio donde ya has disparado vuelves a disparar.
"""

juego = tablero_machine.copy()
disparo = juego[0:10]

disparar_fila = int(input("Selecciona una fila"))
disparar_colm = int(input("Selecciona una columna"))

disparo = juego[disparar_fila,disparar_colm]

# Mientras aciertas
while disparo == 'O':
    juego[disparar_fila,disparar_colm] = 'X'
    print(juego)
    
    disparar_fila = int(input("Selecciona una fila"))
    disparar_colm = int(input("Selecciona una columna"))
    disparo = juego[disparar_fila,disparar_colm]  
    continue

# Si das agua
if disparo != 'O':
    juego[disparar_fila,disparar_colm] = '*'

#Falta si disparo donde ya disparé
while disparo == "X" or disparo == "*":
    print("No puedes disparar ahí, prueba de nuevo")

    disparar_fila = int(input("Selecciona una fila"))
    disparar_colm = int(input("Selecciona una columna"))
    disparo = juego[disparar_fila,disparar_colm]  
    continue


print(juego)