import sqlite3
import csv

# Conexión a la base de datos
conexion = sqlite3.connect('bookmaker.db')


partidos = []

# Crear un cursor
cursor = conexion.cursor()

# Obtener la lista de tablas en la base de datos
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablas = cursor.fetchall()



# Iterar sobre las tablas
for tabla in tablas:
    print("Tabla:", tabla[0])
    print("---------")

    # Obtener los nombres de las columnas de la tabla
    cursor.execute("PRAGMA table_info({})".format(tabla[0]))
    columnas = cursor.fetchall()
    nombres_columnas = [columna[1] for columna in columnas]

    # Obtener los datos de cada columna
    cursor.execute("SELECT * FROM {}".format(tabla[0]))
    filas = cursor.fetchall()

    # Imprimir los nombres de las columnas
    for columna in nombres_columnas:
        print("Columna:", columna)

    print("Datos:")
    # Imprimir los datos de cada columna

    for fila in filas:
        for valor in fila:
            print(valor, end="\t")
            # archivo_csv.write(str(valor))
        print()
    # archivo_csv.close()


    print("\n")
    if tabla[0] == "partidos":
        print("Estoy en partido")
        print("Datos:")
        # Imprimir los datos de cada columna

        for fila in filas:
            partido = []
            for valor in fila:
                print(valor,end="\t")
                valor = str(valor)
                partido.append(valor)

                # archivo_csv.write(str(valor))
            partidos.append(partido)
            print()

aaaaaaaaaaa = open("Partiditos.csv", "w")
with open("Partiditos.csv", "w", newline="") as aaaaaaaaaaa:
    escritor_csv = csv.writer(aaaaaaaaaaa)
    aaaaaaaaaaa.write("id,fecha,equipo_local,equipo_visistante,finalizado,ganador\n")
    for fila in partidos:  
        escritor_csv.writerow(fila)
    aaaaaaaaaaa.close()

    print("\n")

# Cerrar la conexión
conexion.close()




