import numpy as np
import def_barcos_player
import def_barcos_machine


# Primera interación para entrar a jugar.
inicio = input("Para jugar pulsa P, para salir pulsa cualquier tecla")

tablero = np.full((10,10)," ")
tablero_machine = np.full((10,10)," ")

# Presentación de los barcos del jugador.
print("Estos son tus barcos")

if inicio.lower() == "p":
    print(tablero,
          def_barcos_player.colocar_barcos(1),
          def_barcos_player.colocar_barcos(1),
          def_barcos_player.colocar_barcos(1),
          def_barcos_player.colocar_barcos(1),
          def_barcos_player.colocar_barcos(2),
          def_barcos_player.colocar_barcos(2),
          def_barcos_player.colocar_barcos(2),
          def_barcos_player.colocar_barcos(3),
          def_barcos_player.colocar_barcos(3),
          def_barcos_player.colocar_barcos(4))

else:
    print("Adios") #Sino quiere jugar, ha entrado por error.

print("\n")

# Presentación de los barcos del jugador.
print("Estos son los barcos de la máquina")

print(tablero_machine,
      def_barcos_machine.LockIn_maquina(1),
      def_barcos_machine.LockIn_maquina(1),
      def_barcos_machine.LockIn_maquina(1),
      def_barcos_machine.LockIn_maquina(1),
      def_barcos_machine.LockIn_maquina(2),
      def_barcos_machine.LockIn_maquina(2),
      def_barcos_machine.LockIn_maquina(2),
      def_barcos_machine.LockIn_maquina(3),
      def_barcos_machine.LockIn_maquina(3),
      def_barcos_machine.LockIn_maquina(4)) 

#EMPIEZA EL JUEGO

#Mapa en blanco para ir viendo el avance de los disparos del jugador sobre el mapa de la máquina.
juego_player = np.full((10,10)," ")

#Bucle para iniciar y finalizar el juego. 
while True:

    #Herramienta para interrumpir el juego siempre que lo desee el jugador.
    salir = input("pulsa x para salir")
    if salir.lower() == "x":
        break

    #Disparos del juegador.
    while True:

        #Pide coordenadas
        disparar_fila = int(input("Selecciona una fila"))-1
        disparar_colm = int(input("Selecciona una columna"))-1


        #Si acierta, marcas con una X y repites.
        if tablero_machine[disparar_fila][disparar_colm] == "O":
            print("Tocado")
            tablero_machine[disparar_fila][disparar_colm] = "X"
            juego_player[disparar_fila][disparar_colm] = "X"
            print(juego_player)

        #Si fallas, marcas con una * y se acaba el bucle.
        elif tablero_machine[disparar_fila][disparar_colm] == " ":
            print("Agua")
            tablero_machine[disparar_fila][disparar_colm] = "*"
            juego_player[disparar_fila][disparar_colm] = "*"            
            print(juego_player)
            break

        #Si disparas donde ya has dado, repites.     
        elif tablero_machine[disparar_fila][disparar_colm] == "O" or tablero_machine[disparar_fila][disparar_colm] == "*":
            print("Ya has disparado aquí, prueba de nuevo")

    #Final del juego cuando no queden O (Barcos).
    if "O" not in tablero_machine:
        print("Has ganado")
        break

    #Disparos para la máquina
    while True:

        if "O" not in tablero:
            print("Has perdido")
            break

        #Coordenadas aleatorias
        machine_shoot = np.random.randint(10, size = 2)
        shoot_row = machine_shoot[0]
        shoot_col = machine_shoot[1]

        if tablero[shoot_row][shoot_col] == "O":
            print("MAQUINA ha disparado: Tocado")
            tablero[disparar_fila][disparar_colm] = "X"
            print(tablero)

        elif tablero[shoot_row][shoot_col] == " ":
            print("MAQUINA ha disparado: Agua")
            tablero[disparar_fila][disparar_colm] = "*"            
            print(tablero)
            break
        elif tablero[shoot_row][shoot_col] == "O" or tablero[shoot_row][shoot_col] == " ":
            print()