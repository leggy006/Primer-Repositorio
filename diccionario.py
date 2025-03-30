# Tarea: Trabajando con Diccionarios en Python

# 1. Crear un diccionario
informacion_personal = {
    "nombre": "Leslye Valencia",
    "edad": 18,
    "ciudad": "Santo Domingo",
    "profesion": "Ingeniero"
}

# 2. Acceder y modificar valores
      #Acceder al valor asociado con la clave "ciudad"
print("Ciudad original:", informacion_personal["ciudad"])

    #Modificar la ciudad por otra diferente
informacion_personal["ciudad"] = "Puyo"
print("Ciudad modificada:", informacion_personal["ciudad"])

# 3. Verificar Existencia de Claves
    # Verificar si la clave "telefono" existe y agregarla si no está
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0781013573"

# 4. Eliminar una clave
del informacion_personal["edad"]

# 5. Imprimir el diccionario final
print("Diccionario final:", informacion_personal)
