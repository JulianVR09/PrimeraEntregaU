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
            fila.append(".")
        tablero.append(fila)
    return tablero

def mostrarTablero(tablero, columnas):
    # Encabezado con números de columna
    print(" ", end="")
    for i in range(1, columnas + 1):
        print(f" {i}", end="")
    print()

    # Línea separadora superior
    print("+", end="")
    for i in range(columnas):
        print("- ", end="")
    print("+")                                     # Esta función es para mostrar el tablero

    # Filas del tablero
    for fila in tablero:
        print("|", end="")
        for casilla in fila:
            print(f"{casilla} ", end="")
        print("|")

    # Línea separadora inferior
    print("+", end="")
    for i in range(columnas):
        print("- ", end="")
    print("+")
        
def colocarFicha(tablero, columna, simbolo):
    filas = len(tablero)
    columnaIndex = columna - 1
    
    for fila in range(filas -1, -1, -1):            # Esta función es para colocar la ficha, esta busca la ultima fila, y se va devolviendo de la ultima hasta la primera y de alli no pasa
        if tablero[fila][columnaIndex] == ".":
            tablero[fila][columnaIndex] = simbolo
            return True
    
    return False

def validacionJuego(columna, totalColumnas, tablero):
    if columna < 1 or columna > totalColumnas:
        print("La columna debe estar entre 1 y", totalColumnas)
        return False
                                                                            #Verifica si la columna que se envio si exista en el tablero y si esta llena
    # Verificar si la columna está llena
    if tablero[0][columna - 1] != ".":
        print("La columna está llena, selecciona otra")
        return False
    
    return True

def obtenerColumnasDisponibles(tablero, totalColumnas):
    columnas_disponibles = []
    for columna in range(1, totalColumnas + 1):
        if validacionJuego(columna, totalColumnas, tablero):
            columnas_disponibles.append(columna)
    return columnas_disponibles

def verificarVictoria(tablero, filas, columnas, simbolo):
    # Verificar horizontal
    for fila in range(filas):
        for col in range(columnas - 3):
            if all(tablero[fila][col + i] == simbolo for i in range(4)):
                return True
    
    # Verificar vertical
    for fila in range(filas - 3):
        for col in range(columnas):
            if all(tablero[fila + i][col] == simbolo for i in range(4)):
                return True
    
    # Verificar diagonal descendente
    for fila in range(filas - 3):
        for col in range(columnas - 3):
            if all(tablero[fila + i][col + i] == simbolo for i in range(4)):
                return True
    
    # Verificar diagonal ascendente
    for fila in range(3, filas):
        for col in range(columnas - 3):
            if all(tablero[fila - i][col + i] == simbolo for i in range(4)):
                return True
    
    return False

def tableroLleno(tablero):
    for fila in tablero:
        if "." in fila:
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
        print(f"\nTurno de {jugadorActual}")
        print("1. Seleccionar columna manualmente")
        print("2. Seleccionar columna aleatoriamente")
        
        opcion = enteroValido("Seleccione una opción (1 o 2): ")
        
        if opcion == 1:
            columna = enteroValido("Ingrese la columna donde desea colocar su ficha: ")
            if validacionJuego(columna, totalColumnas, tablero):
                return columna
        elif opcion == 2:
            columnas_disponibles = obtenerColumnasDisponibles(tablero, totalColumnas)
            if columnas_disponibles:
                columna = random.choice(columnas_disponibles)
                print(f"Columna seleccionada aleatoriamente: {columna}")
                return columna
            else:
                print("No hay columnas disponibles")
        else:
            print("Opción inválida. Seleccione 1 o 2")

def tableroATexto(tablero, columnas):
    # Genera la representación en texto del tablero para las estadísticas
    texto = ""
    
    # Encabezado con números de columna
    texto += " "
    for i in range(1, columnas + 1):
        texto += f" {i}"
    texto += "\n"

    # Línea separadora superior
    texto += "+"
    for i in range(columnas):
        texto += "- "
    texto += "+\n"

    # Filas del tablero
    for fila in tablero:
        texto += "|"
        for casilla in fila:
            texto += f"{casilla} "
        texto += "|\n"

    # Línea separadora inferior
    texto += "+"
    for i in range(columnas):
        texto += "- "
    texto += "+\n"
    
    return texto

def generarEstadisticas(jugador1, jugador2, partidas_jugadas, victorias_j1, victorias_j2, empates, tableros_finales, resultados):
    # Generar documento con estadísticas
    with open("estadisticas.txt", "w", encoding="utf-8") as archivo:
        archivo.write("==============================================\n")
        archivo.write("==== Estadísticas de la sesión de juego ====\n")
        archivo.write(f"Nombre del jugador 1: {jugador1} (X)\n")
        archivo.write(f"Nombre del jugador 2: {jugador2} (O)\n")
        archivo.write(f"Número de partidas jugadas: {partidas_jugadas}\n")
        archivo.write(f"Número de victorias de {jugador1}: {victorias_j1}\n")
        archivo.write(f"Número de victorias de {jugador2}: {victorias_j2}\n")
        archivo.write(f"Número de empates: {empates}\n")
        
        for i, (tablero, resultado) in enumerate(zip(tableros_finales, resultados)):
            archivo.write(f"==== Tablero al final de la partida #{i+1} ====\n")
            archivo.write(tablero)
            archivo.write(f"{resultado}\n")
        
        archivo.write("==============================================\n")
    
    print("Estadísticas guardadas en 'estadisticas.txt'")

def jugarPartida():
    # Obtener nombres de jugadores (solo la primera vez)
    jugador1, jugador2 = obtenerDatosJugadores()
    
    # Variables para estadísticas
    partidas_jugadas = 0
    victorias_j1 = 0
    victorias_j2 = 0
    empates = 0
    tableros_finales = []
    resultados = []
    
    while True:
        partidas_jugadas += 1
        print(f"\n{'='*50}")
        print(f"PARTIDA #{partidas_jugadas}")
        print(f"{'='*50}")
        
        # Obtener dimensiones del tablero para cada partida
        filas, columnas = obtenerDimensiones()
        tablero = crearTablero(filas, columnas)
        
        # Decidir quién inicia aleatoriamente
        jugadores = [jugador1, jugador2]
        simbolos = ["X", "O"]
        turnoActual = random.randint(0, 1)
        
        print(f"\n{jugador1} jugará con 'X' y {jugador2} jugará con 'O'")
        print(f"{jugadores[turnoActual]} iniciará la partida")
        print("\nTablero inicial:")
        mostrarTablero(tablero, columnas)
        
        # Jugar la partida
        while True:
            jugadorActual = jugadores[turnoActual]
            simboloActual = simbolos[turnoActual]
            
            columnaElegida = obtenerJugada(jugadorActual, columnas, tablero)
            colocarFicha(tablero, columnaElegida, simboloActual)
            
            print(f"\n{jugadorActual} colocó una ficha en la columna {columnaElegida}")
            mostrarTablero(tablero, columnas)
            
            # Verificar victoria
            if verificarVictoria(tablero, filas, columnas, simboloActual):
                mensaje_resultado = f"{jugadorActual} ({simboloActual}) ha ganado la partida :)"
                print(f"\n¡{mensaje_resultado}")
                
                # Actualizar estadísticas
                if turnoActual == 0:
                    victorias_j1 += 1
                else:
                    victorias_j2 += 1
                
                tableros_finales.append(tableroATexto(tablero, columnas))
                resultados.append(mensaje_resultado)
                break
            
            # Verificar empate
            if tableroLleno(tablero):
                mensaje_resultado = "La partida ha terminado en un empate :c"
                print(f"\n{mensaje_resultado}")
                empates += 1
                tableros_finales.append(tableroATexto(tablero, columnas))
                resultados.append(mensaje_resultado)
                break
            
            # Cambiar turno
            turnoActual = 1 - turnoActual
        
        # Preguntar si desea jugar otra ronda
        print("\n¿Desea jugar otra ronda?")
        while True:
            continuar = input("Ingrese 's' para sí o 'n' para no: ").lower().strip()
            if continuar in ['s', 'si', 'sí']:
                break
            elif continuar in ['n', 'no']:
                # Generar estadísticas y finalizar
                print("\n¡Gracias por jugar Connect 4!")
                generarEstadisticas(jugador1, jugador2, partidas_jugadas, victorias_j1, victorias_j2, empates, tableros_finales, resultados)
                return
            else:
                print("Por favor, ingrese 's' para sí o 'n' para no")

# Ejecutar el juego
jugarPartida()