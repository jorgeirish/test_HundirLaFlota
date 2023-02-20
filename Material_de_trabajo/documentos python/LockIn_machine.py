import numpy as np

# Tablero selección barcos 10x10 con agua

def LockIn(): 

    tablero_machine = np.full((10,10),"~")

    print("Estos son tus barcos")

    def colocar_barcos(barco):

        eslora = barco
        import random

        while True:
            # 'N' - 'S' - 'E' - 'O'
            orient = random.choice(['N', 'S', 'E', 'O'])

            # Posicion inicial del barco
            current_pos = np.random.randint(10, size = 2)
    
            fila = current_pos[0]
            col = current_pos[1]
    
            # Recogemos las 4 posiciones colindantes a current_pos
            coors_posN = tablero_machine[fila:fila - eslora:-1, col]
            coors_posE = tablero_machine[fila, col: col + eslora]
            coors_posS = tablero_machine[fila:fila + eslora, col]
            coors_posO = tablero_machine[fila, col: col - eslora:-1]
    
            # Comprobamos si esas posiciones son validas
            # Orientacion Norte
            if orient == 'N' and 0 <= fila - eslora < 10 and 'O' not in coors_posN:
                tablero_machine[fila:fila - eslora:-1, col] = 'O'
                break

            # Orientacion Este
            elif orient == 'E' and 0 <= col + eslora < 10 and 'O' not in coors_posE:
                tablero_machine[fila, col: col + eslora] = 'O'
                break

            # Orientacion Sur
            elif orient == 'S' and 0 <= fila + eslora < 10 and 'O' not in coors_posS:
                tablero_machine[fila:fila + eslora, col] = 'O'
                break

            # Orientacion Oeste
            elif orient == 'O' and 0 <= col - eslora < 10 and 'O' not in coors_posO:
                tablero_machine[fila, col: col - eslora:-1] = 'O'
                break

            # No cumple con las dimensiones del tablero, o hay un barco ahi
            # Probamos con otra coordenada
            else:
                continue
        return ""

    print(tablero_machine,
colocar_barcos(1),
colocar_barcos(1),
colocar_barcos(1),
colocar_barcos(1),
colocar_barcos(2),
colocar_barcos(2),
colocar_barcos(2),
colocar_barcos(3),
colocar_barcos(3),
colocar_barcos(4))