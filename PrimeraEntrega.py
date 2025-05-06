import sys;

print ("bienvenidos a conecta4 de fundamentos de programcion");
jugador1 = input("Ingrese el nombre del primer jugador: ");
jugador2 = input("Ingrese el nombre del segundo jugador: ");

if(len(jugador1) < 1 or len(jugador2) < 1) : #validación de que los campos no esten vacios
    print("El nombre de los jugadores debe tener al menos un caracter");
    sys.exit()
    
elif(jugador1 == jugador2) : #validacion de que los nombres de los jugadores no sean iguales
    print("Los nombres de los jugadores no pueden ser iguales");
    sys.exit()
    
fila = int(input("Ingrese el numero de filas con las que desea jugar: "));
columna = int(input("Ingrese el numero de columnas con las que desea jugar: "));

    
if(fila < 3 or columna < 3) : #validación de que el numero de filas y columnas sea mayor a 3
    print("El numero de filas y columnas debe ser mayor a 3");
    sys.exit()
    
for i in range (1, columna + 1):
    print(f" {i}", end="") #imprime los numeros de las columnas en la primera fila
    
print();


for i in range (columna) :
    print(" =", end=""); #imprime los iguales despues de los numeros de las columnas y estos delimitaran el tablero

print();


for i in range (fila) :
    print("|", end=""); #imprime barra despues de los iguales y este delimitara el tablero
    for j in range (columna) :
        print("* ", end=""); #imprime las casillas del tablero que seran vistas como asteriscos
        
    print("|"); #imprime barra despues de los iguales y este delimitara el tablero
    
for i in range (columna) :
    print(" =", end=""); #imprime los iguales despues de todos los asteriscos y estos delimitaran el tablero

print();

while(True) :
    print(f"Turno de {jugador1}");
    posicion = int(input("Ingrese el numero de la columna donde desea poner su ficha: "));
    
    
    print(f"Turno de {jugador2}");