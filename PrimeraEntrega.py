import sys;

print ("bienvenido a conecta4 de fundamentos de programcion");
jugador1 = input("Ingrese el nombre del primer jugador: ");
jugador2 = input("Ingrese el nombre del segundo jugador: ");
fila = int(input("Ingrese el numero de filas con las que desea jugar: "));
columna = int(input("Ingrese el numero de columnas con las que desea jugar: "));

if(len(jugador1) < 3 or len(jugador2) < 3) :
    print("El nombre de los jugadores debe ser mayor a 3 caracteres");
    sys.exit()
    
if(fila < 3 or columna < 3) :
    print("El numero de filas y columnas debe ser mayor a 3");
    sys.exit()