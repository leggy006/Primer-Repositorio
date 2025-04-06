# TAREA: Trabajo con Archivos de Texto en Python

# ----------- ESCRITURA DE ARCHIVO -----------
# Creamos y abrimos el archivo 'my_notes.txt' en modo escritura ('w')
# El archivo no existe por lo que lo creará automáticamente
archivo = open("my_notes.txt", "w")

# Escribimos 3 líneas de notas personales
archivo.write("Estas son mis notas personales:\n")
archivo.write("1. Entregar el práctico experimental de física.\n")
archivo.write("2. Terminar de pintar el lienzo.\n")
archivo.write("3. Grabar el audiolibro de Inglés.\n")

# Cerramos el archivo después de escribir
archivo.close()


# ----------- LECTURA DE ARCHIVO -----------
# Abrimos el archivo 'my_notes.txt' en modo lectura ('r')
archivo = open("my_notes.txt", "r")

# Leemos el contenido línea por línea y lo mostramos en pantalla
linea = archivo.readline()  # Leer la primera línea

while linea:  # Mientras haya líneas por leer
    print(linea.strip())  # Mostrar la línea (strip() elimina saltos de línea extra)
    linea = archivo.readline()  # Leer la siguiente línea

# Cerramos el archivo después de leer
archivo.close()
