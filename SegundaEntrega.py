def validacionNombre(nombre):
    if(len(nombre) < 1 or len(nombre) > 10):
        print("El nombre de los jugadores debe tener al menos un caracter y no puede exceder los 10 caracteres")
        return False
    
    if not nombre.isalpha():
        print("El nombre de los jugadores debe contener solo letras")
        return False
    
    return True

def validacionFilaColumna(fila, columna):
    if(fila < 3 or columna < 3):  
        print("El numero de filas y columnas debe ser mayor a 3")
        return False
    
    return True

def validacionJugadores(jugador1, jugador2):
    if(jugador1.lower() == jugador2.lower()):
        print("Los nombres de los jugadores no pueden ser iguales")
        return False
    
    return True

def validacionJuego(columna, totalColumnas, tablero):
    if columna < 1 or columna > totalColumnas:
        print(f"La columna debe estar entre 1 y {totalColumnas}")
        return False
    
    # Verificar si la columna está llena
    if tablero[0][columna - 1] != "*":
        print("La columna está llena, selecciona otra")
        return False
    
    return True

def crearTablero(filas, columnas):
    tablero = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append("*")
        tablero.append(fila)
    return tablero

def mostrarTablero(tablero, columnas):
    for i in range(1, columnas + 1):
        print(f" {i}", end="")
    print()
    
    for i in range(columnas):
        print(" =", end="")
    print()
    
    for fila in tablero:
        print("|", end="")
        for casilla in fila:
            print(f"{casilla} ", end="")
        print("|")
    
    for i in range(columnas):
        print(" =", end="")
    print()

def colocarFicha(tablero, columna, simbolo):
    filas = len(tablero)
    columnaIndex = columna - 1
    
    for fila in range(filas - 1, -1, -1):
        if tablero[fila][columnaIndex] == "*":
            tablero[fila][columnaIndex] = simbolo
            return True
    
    return False

def obtenerDatosJugadores():
    print("¡Bienvenidos al juego Connect 4!")
    
    # Validar primer jugador
    while True:
        jugador1 = input("Ingrese el nombre del primer jugador: ").strip()
        if validacionNombre(jugador1):
            break
    
    # Validar segundo jugador
    while True:
        jugador2 = input("Ingrese el nombre del segundo jugador: ").strip()
        if validacionNombre(jugador2):
            if validacionJugadores(jugador1, jugador2):
                break
            else:
                continue
    
    return jugador1, jugador2

def obtenerDimensiones():
    while True:
        filas = int(input("Ingrese el numero de filas con las que desea jugar: "))  
        columnas = int(input("Ingrese el numero de columnas con las que desea jugar: "))
    
        if validacionFilaColumna(filas, columnas):
            return filas, columnas

def obtenerJugada(jugadorActual, totalColumnas, tablero):
    while True:
        columna = int(input(f"Turno de {jugadorActual}. Ingrese la columna donde desea colocar su ficha: "))
            
        if validacionJuego(columna, totalColumnas, tablero):
            return columna

def jugarPartida():
    # Obtener datos iniciales
    jugador1, jugador2 = obtenerDatosJugadores()
    filas, columnas = obtenerDimensiones()
    
    # Crear tablero
    tablero = crearTablero(filas, columnas)
    
    # Configurar juego
    jugadores = [jugador1, jugador2]
    simbolos = ["X", "O"]
    turnoActual = 0
    
    print(f"\n{jugador1} jugará con 'X' y {jugador2} jugará con 'O'")
    print("\nTablero inicial:")
    mostrarTablero(tablero, columnas)
    
    # Bucle principal del juego
    while True:
        jugadorActual = jugadores[turnoActual]
        simboloActual = simbolos[turnoActual]
        
        # Obtener jugada válida
        columnaElegida = obtenerJugada(jugadorActual, columnas, tablero)
        
        # Colocar ficha
        colocarFicha(tablero, columnaElegida, simboloActual)
        
        # Mostrar tablero actualizado
        print(f"\n{jugadorActual} colocó una ficha en la columna {columnaElegida}")
        mostrarTablero(tablero, columnas)
        
        # Cambiar turno
        turnoActual = 1 - turnoActual  # Alterna entre 0 y 1

# Ejecutar el juego
if __name__ == "__main__":
    jugarPartida()