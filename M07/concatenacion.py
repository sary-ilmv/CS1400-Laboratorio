"""
M7 Laboratorio presencial:
Elije una pareja para entrevistar.
La concatenación de cadenas para aprender a usar + y unir cadenas de texto.
Incluir espacios manualmente (" "), y combinar entrada del usuario con otros textos.
"""

# TODO Tarea 1: Escribe una linea de bienvenida a este programa

print("¡Bienvenida al programa de entrevista!")


# TODO Tarea 2: Solicitar datos del usuario.
# Usar tres variables: nombre, apellido, y cancion.
# Entrevista algun companero(a) para averiguar su cancion preferida y su nombre completo.

nombre = input("Escribe tu primer nombre: ")
apellido = input("Escribe tu apellido: ")
cancion = input("¿Cuál es tu canción favorita? ")

# Una manera de validar entradas vacías
# Toma en cuenta que cambios podrias realizar si tienen un segundo nombre, y/o un segundo apellido.
# La meta es obtener su nombre completo.

if not nombre.strip():
    print("Por favor, escribe tu primer nombre.")
    exit()

if not apellido.strip():
    print("Por favor, escribe tu apellido.")
    exit()

if not cancion.strip():
    print("Por favor, escribe el nombre de una canción que te guste.")
    exit()

# Formatear entrada: capitalizar nombres
# Agregar nuevos variables si es necesario.

nombre = nombre.strip().capitalize()
apellido = apellido.strip().capitalize()
cancion = cancion.strip().title()

# TODO Tarea 3: Crear una variable llamada nombre_completo para juntar
# (concatenar) todos los nombres ingresados, usando los espacios adecuados.

nombre_completo = "Grecia Sariah Lopez Orozco"

# TODO Tarea 4: Mostrar el resultado con alguna frase como por ejemplo,
# "Tu nombre completo es ___"

print("Tu nombre completo es " + nombre_completo)


# TODO Tarea 5: Crear un último variable, y agrégale más texto concatenado.
# Puede ser un saludo, o un piropo que incluya la variable para la canción.

mensaje = "Hola " + nombre_completo + ", me encanta que tu canción favorita sea " + cancion + "!"

# Imprimir a la terminal

print(mensaje)
