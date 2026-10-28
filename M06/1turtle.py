""" TODO 1 Grecia
Tortuga
octubre 2026
"""


# Importamos la biblioteca turtle (ya viene incluida en Python)
import turtle

# Configuración de la pantalla y la tortuga
pantalla = turtle.Screen() # # Usamos sintaxis de punto . para acceder a la función Screen()
pantalla.bgcolor("darkgray")  

# TODO 2 Cambia el color de fondo usando la función bgcolor()
pantalla.title("Tortuga pequena") 

#TODO 3 Asigna un título a la ventana usando title()

# Corre el programa hasta este punto utilizando """ """ o # para asegurar que funcione bien.

# solo una t para hacer menos codigo despues. usaremos la t variable para usar otras funciones.
t = turtle.Turtle()
t.shape("turtle")  # Forma de la tortuga puede ser cualquier otro nombre.
t.speed(3)         # Velocidad del dibujo (1 es lento, 10 es rápido)

# TODO 4 para correr el programa hasta este punto y toma una captura de pantalla. Luego lo guardaras entre la carpeta M6


# =============================================================
# EJEMPLO: Dibujar la base de la casa (un cuadrado azul)
# =============================================================

t.color("black", "white")  # (Color del borde, Color de relleno - los puedes ajustar si deseas -
TODO 5 los colores son parametros o argumentos?)
Son argumentos porque "black" y "white" son los valores que se le dan a la función t.color()
t.begin_fill()

# TODO 6 Este for loop que hace?
# Repite el codigo cuatro veces para dibujar un cuadrado. La tortuga avanza 100 unidades y gira 90 grados en cada repeticion.

for _ in range(4):
    t.forward(100)  # este numero mide la altura en que la tortuga va a ir lo que significa que estaso dos de 90 y 100 va a girar y avanzar
    t.left(90)      # este numero define en que longitud la tortuga va a llegar para llegar a hacer un cuadro

# TODO 7 En que linea de codigo empezo el fill? o relleno?
# El relleno empezo en la línea t.begin_fill()
#  t.end_fill() # Termina el relleno del cuadrado

# Mantiene la ventana abierta hasta que hagas clic en ella
pantalla.exitonclick()
