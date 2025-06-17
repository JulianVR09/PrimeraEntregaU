import random

def enteroValido(mensaje):
    while True:
        try:
            posibleEntero = int(input(mensaje))
            return posibleEntero                    # Esta función es para validar que el usuario ingrese un entero
        except ValueError:
            print("Debe ingresar un entero")
            continue
            
def solicitarColumnas():
    while True:
        columnas = enteroValido("Ingrese el numero de columnas con las que desea jugar: ")
        if columnas <= 3:                                                                       # Esta función es para verificar que cuadno se pida un numero este sea mayor que 3 para las columnas
            print("El numero de columnas debe ser mayor a 3")
            continue
        else:
            return columnas

def solicitarFilas():
    while True:
        filas = enteroValido("Ingrese el numero de filas con las que desea jugar: ")
        if filas <= 3:                                                                          # Esta función es para verificar que cuadno se pida un numero este sea mayor que 3 para las filas
            print("El numero de filas debe ser mayor a 3")
            continue
        return filas
        
def crearTablero(filas, columnas):
    tablero = []
    for i in range(filas):
        fila = []                       #Esta función es para crear la matrix donde se van a guaradar las listas que contengan los movimientos
        for j in range(columnas):
            fila.append("*")
        tablero.append(fila)
    return tablero

def mostrarTablero(tablero, columnas):
    # Encabezado con números de columna
    print("|", end="")
    for i in range(1, columnas + 1):
        print(f"{i}", end="|")
    print()

    # Línea separadora superior
    print("|", end="")
    for i in range(columnas):
        print("=", end="|")
    print()                                     # Esta función es para mostrar el tablero

    # Filas del tablero
    for fila in tablero:
        print("|", end="")
        for casilla in fila:
            print(f"{casilla}", end="|")
        print()

    # Línea separadora inferior
    print("|", end="")
    for i in range(columnas):
        print("=", end="|")
    print()
        
def colocarFicha(tablero, columna, simbolo):
    filas = len(tablero)
    columnaIndex = columna - 1
    
    for fila in range(filas -1, -1, -1):            # Esta función es para colocar la ficha, esta busca la ultima fila, y se va devolviendo de la ultima hasta la primera y de alli no pasa
        if tablero[fila][columnaIndex] == "*":
            tablero[fila][columnaIndex] = simbolo
            return True
    
    return False

def validacionJuego(columna, totalColumnas, tablero):
    if columna < 1 or columna > totalColumnas:
        print("La columna debe estar entre 1 y", totalColumnas)
        return False
                                                                            #Verifica si la columna que se envio si exista en el tablero y si esta llena
    # Verificar si la columna está llena
    if tablero[0][columna - 1] != "*":
        print("La columna está llena, selecciona otra")
        return False
    
    return True
        
def validacionNombre(nombre):
    if(len(nombre) < 1 or len(nombre) > 10):
        print("El nombre de los jugadores debe tener al menos un caracter y no puede exceder los 10 caracteres")
        return False
                                                                            #Verifica si el nombre de los jugadores contienen solo letras y no exceden los 10 caracteres 
    if not nombre.isalpha():
        print("El nombre de los jugadores debe contener solo letras")
        return False
    
    return True

def validacionJugadores(jugador1, jugador2):
    if(jugador1.lower() == jugador2.lower()):
        print("Los nombres de los jugadores no pueden ser iguales")         #Verifica si los nombres de los jugadores son iguales
        return False
    
    return True

def obtenerDatosJugadores():
    print("¡Bienvenidos al juego Connect 4!")
    
    while True:
        jugador1 = input("Ingrese el nombre del primer jugador: ").strip()
        if validacionNombre(jugador1):
            break
        
    while True:
        jugador2 = input("Ingrese el nombre del segundo jugador: ").strip()             #Pide los nombres de los jugadores y verifica si son validos, ademas de no ser iguales
        if validacionNombre(jugador2):
            if validacionJugadores(jugador1, jugador2):
                break
            else:
                continue
    
    return jugador1, jugador2

def obtenerDimensiones():
    filas = solicitarFilas()
    columnas = solicitarColumnas()
    return filas, columnas

def obtenerJugada(jugadorActual, totalColumnas, tablero):
    while True:
        columna = enteroValido(f"Turno de {jugadorActual}. Ingrese la columna donde desea colocar su ficha: ")  #Pide la jugada y verifica si es valida
            
        if validacionJuego(columna, totalColumnas, tablero):
            return columna
        
def jugarPartida():
    
    jugador1, jugador2 = obtenerDatosJugadores()
    filas, columnas = obtenerDimensiones()
    
    
    tablero = crearTablero(filas, columnas)
    
   
    jugadores = [jugador1, jugador2]                                #Función para iniciar el juego, pidiendo las cosas claves, como :  nombres de los jugadores, filas y columnas
    simbolos = ["X", "O"]
    turnoActual = random.randint(0, 1)
    
    print(f"\n{jugador1} jugará con 'X' y {jugador2} jugará con 'O'")
    print("\nTablero inicial:")
    mostrarTablero(tablero, columnas)
    
    while True:
        jugadorActual = jugadores[turnoActual]
        simboloActual = simbolos[turnoActual]
        
        columnaElegida = obtenerJugada(jugadorActual, columnas, tablero)
        
        colocarFicha(tablero, columnaElegida, simboloActual)                            #Función para colocar la ficha y cambiar el turno
        
        print(f"\n{jugadorActual} colocó una ficha en la columna {columnaElegida}")
        mostrarTablero(tablero, columnas)
        
        # Cambiar turno
        turnoActual = 1 - turnoActual
        
jugarPartida() #llamado de la funcion principal que inicia el juego